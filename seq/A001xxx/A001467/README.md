# A001467

> Denominators of an expansion for Pi.
> — [OEIS A001467](https://oeis.org/A001467)

Offset 0: 1, 1, 1, 7, -791, -3748629, 151648960887729, -1323497544567561138595307148089, …

### Python 3 — 152 bytes

```python
print('1\n1\n1');q=t=l=y=1
while any(4*(t-(c:=(2*t+y)//(y-~y))*Y)**2>Y*Y for Y in(y,y-q))or[print(c),y:=y*c-t,q:=q*c,t:=t*c]:l+=2;y=y*l-2*q;q*=l//2;t*=l
```

**How it works**

- **The definition.** The title only says "an expansion"; the entry
  pins it down in its example and PARI program: start with x = π; at each
  step take d = 1 while x ≥ 1, and otherwise the integer nearest to 1/x
  ("closer to 1/(−791) than to 1/(−790)"); print d and go on with
  x − 1/d. All 9 terms of the b-file agree with this. Since π is
  irrational, x is never 0 and 1/x is never halfway between two integers.
- **The first three terms.** 3 < π < 4, so x = π, π − 1, π − 2 are all ≥ 1
  and give d = 1; then x = π − 3 lies in (0, 1). From there on |x| < 1
  forever: if d is the integer nearest to 1/x, then |x − 1/d| =
  |x|·|d − 1/x|/|d| < |x|/(2|d|) ≤ |x|/2. So the rule d = 1 never applies
  again, d is always the nearest integer to 1/x, and the program prints
  the three 1's and starts at x = π − 3.
- **π from Gibbons' spigot**, the same state as the π digits of
  [A000796](../../A000xxx/A000796/): the series
  π = 2 + 1/3·(2 + 2/5·(2 + 3/7·(2 + …))) is read term by term into a map
  f(X) = (q·X + y − 4q)/t with q/t > 0, and x = f(X) for the value X of the
  rest of the series, strictly between 3 and 4. So x lies strictly between
  f(3) = (y − q)/t and f(4) = y/t. A new term (`l` = 2k + 1, `l//2` = k)
  turns f into f(2 + k·X/l): q → q·k, t → t·l, y → y·l − 2q, and the
  interval gets more than 2 times narrower. q = t = y = 1 at the start
  gives f(X) = X − 3.
- **Checking a candidate.** c = d means |1/x − c| < 1/2, that is
  4(1 − c·x)² < x², or h(x) = x² − 4(1 − c·x)² > 0. For c ≠ 0, h is a
  quadratic with leading coefficient 1 − 4c² < 0, so it is concave: if
  h ≥ 0 at both ends f(3), f(4), it is > 0 at every point strictly
  between, x included, and then d = c. At Y/t (Y = y − q or y), t²·h is
  Y² − 4(t − c·Y)², the test in `any`. The candidate is
  c = ⌊(2t + y)/(2y + 1)⌋ (`y-~y` = 2y + 1, never 0), close to the nearest
  integer to t/y = 1/f(4). If c = 0 the test fails, since it would need
  |f(3)| and |f(4)| ≥ 2 while x is within the interval width (at most 1)
  of both and |x| < 1. A test that fails just reads another term.
- **It never stalls.** As terms come in, y/t and (y − q)/t tend to x and
  t to infinity, so the candidate tends to ⌊1/x + 1/2⌋ = d (1/x + 1/2 is
  never a whole number), and h at both ends tends to h(x) > 0.
- **Taking the step.** x − 1/c = (c·(q·X + y − 4q) − t)/(c·t):
  q → q·c, t → t·c, y → y·c − t, exact. When c < 0 this makes q and t
  negative, which is fine: q/t stays positive (f still increases), the test
  only uses t², and the candidate only the ratio t/y. The list holding the
  print is non-empty, so the body also runs after a print.

**Notes**

- Exact integer arithmetic, so it is right for every n. The denominators
  roughly double in length at each step: a(9) has 125 digits, a(11) 501,
  and a(14) about 4000; a(15) would pass the 4300-digit int-to-str limit
  of Python 3.11+, an interpreter limit far beyond the b-file. The 9-term
  b-file prints at once; a(11) takes about 4 s and a(12) about 30 s on a
  slow PC. The bar is the whole b-file in 60 s.
- Handling the rule x ≥ 1 in the loop instead of printing the three 1's,
  with the test `and y-q<t` and the candidate `…or 1` (which needs t > 0,
  so steps scaled by c² instead of c), is 159 bytes.
- [A001466](../A001466/) is the greedy (ceiling) expansion of π − 3 with
  the same π state.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 152 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001467), CC BY-SA 4.0.
