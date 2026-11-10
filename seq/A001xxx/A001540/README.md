# A001540

> Number of transpositions needed to generate permutations of length n.
> — [OEIS A001540](https://oeis.org/A001540)

Offset 1: 0, 2, 8, 36, 184, 1110, 7776, 62216, 559952, 5599530, 61594840, …

### Python 3 — 36 bytes

```python
b=n=1
while[print(b-1)]:n+=1;b=b*n|1
```

**How it works**

- The entry gives the e.g.f. cosh(x)/(1 − x) − exp(x), that is
  a(n) = n!·Σ_{k≤n/2} 1/(2k)! − 1, and the recurrence
  a(n) = n·a(n−1) + n − (n mod 2). The program keeps
  b(n) = a(n) + 1 = Σ_{k≤n/2} n!/(2k)! (the coefficients of
  cosh(x)/(1 − x)). Splitting off the last term,
  b(n) = n·b(n−1) + [n even]: every term with 2k ≤ n − 1 is n times its
  counterpart in b(n−1), and the term n!/n! = 1 is there only when n is
  even. This is the entry's recurrence for a(n) = b(n) − 1.
- Every b(n) is odd: b(1) = 1; for n even, n·b(n−1) is even and the +1 makes
  it odd; for n odd, n·b(n−1) is odd times odd. So adding [n even] is the
  same as setting the last bit: `b=b*n|1` adds 1 exactly when n·b(n−1) is
  even, that is when n is even.
- `b=n=1` starts at b(1) = 1, and `print(b-1)` gives a(n).

**Notes**

- Keeping a(n) itself, `a=0;n=1` / `while[print(a)]:n+=1;a=-~a*n&-2`, is 39
  bytes (all a(n) are even, so `&-2` subtracts 1 exactly when n is odd).
- a(n) = |A009179(n)| − 1 (entry).
- Exact integer arithmetic, so the program is right for every n; a(n) is
  about 1.54·n!, so Python's 4300-digit int-to-str limit stops it at about
  n = 1560.
- The b-file has 450 terms (a(1) to a(450)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 36 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001540), CC BY-SA 4.0.
