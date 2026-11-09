# A001273

> Smallest number that takes n steps to reach 1 under iteration of sum-of-squares-of-digits map (= smallest "happy number" of height n).
> — [OEIS A001273](https://oeis.org/A001273)

Offset 0: 1, 10, 13, 23, 19, 7, 356, 78999, …

With s(x) the sum of the squares of the decimal digits of x, the height of a
happy number k is the number of steps k → s(k) → … that reach 1; a(n) is the
least k of height exactly n. The next term, a(8) = 3789·10⁹⁷³ − 1, has 977
digits.

### Python 3 — 101 bytes

```python
n=0
while 1:k=x=0;exec('while x-1:x=k=k+1;'+'x=sum(int(d)**2for d in str(x)[x<2:]);'*n);print(k);n+=1
```

**How it works**

- Let g(x) = s(x) for x ≥ 2 and g(1) = g(0) = 0: `str(x)[x<2:]` drops the
  single digit of 0 and 1, so the sum is empty. Since s(x) ≥ 1 for x ≥ 1, a
  value that reaches 1 becomes 0 at the next step and stays 0. So gⁿ(k) = 1
  exactly when k reaches 1 after n steps and not before: if earlier, it is
  0 by then; if later or never (an unhappy number ends in the cycle 4 → 16 →
  37 → 58 → 89 → 145 → 42 → 20 → 4), it is not 1 yet.
- For each n the program builds and runs, once, the source
  `while x-1:x=k=k+1;x=g(x);…;x=g(x)` with n copies of
  `x=sum(int(d)**2for d in str(x)[x<2:])`. It tries k = 1, 2, 3, … in
  order and stops at the first k with gⁿ(k) = 1, which is a(n); `k=x=0`
  restarts the search at 1 for every n (the terms are not increasing:
  a(5) = 7 < a(4) = 19).
- Every n has a term: a number m of height h ≥ 1 gives the repunit 11…1 with
  m ones, of height h + 1, since s maps it to m. So each search ends, and
  the program never stops by itself.

**Notes**

- a(8) = 3789·10⁹⁷³ − 1 (3788 followed by 973 nines) and a(9) =
  78889·10^((a(8) − 305)/81) − 1, per the OEIS comments, so no search reaches
  them: after a(7) the program keeps searching for a(8) forever. Python's
  4300-digit limit on `str` would only matter for k with more than 4300
  digits.
- Each n's loop is compiled once and then runs in the interpreter; a(7)
  arrives after about 0.8 s here. Running the n steps with `exec` for every
  k (`x=k=k+1;exec('x=…;'*n)`, 98 bytes) compiles the string 79 000 times:
  a(7) comes after about 39 reference seconds, over the limit of 30. A loop over k with a step counter
  (`while~-x*i:x=s(x);i-=1`, then `x+i<2`) is 104 bytes, and with g and
  `for _ in[0]*n:` 103.
- The b-file is synthesized from the 8 terms of the entry; the bar is all 8
  terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001273), CC BY-SA 4.0.
