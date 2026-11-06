# A000323

> Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi*n, P(n) = A(n) - V(n);
> A000099 gives values of n where |P(n)| sets a new record; sequence gives
> A(A000099(n)).
> — [OEIS A000323](https://oeis.org/A000323)

Offset 1: 5, 9, 21, 37, 69, 69, 89, 137, 177, 421, 481, 657, 749, 885, …

### Python 3 — 177 bytes

```python
from math import*
n=a=m=0
while S:=9**isqrt(n:=n+1):
 x=p=2*S;i=A=1
 while x:x=x*i//(i-~i);p+=x;A+=i*i<=n and 4+4*isqrt(n-i*i);i+=1
 if abs(A*S-p*n)>abs(a*S-p*m):m=n;print(a:=A)
```

**How it works**

- The program of [A000099](../A000099/), which finds the record n, with the
  last statement turned round: `m=n;print(a:=A)` prints A(n) instead of n,
  at the same length. The record pair (a, m) = (A(m), m) is kept exactly
  as there.
- One loop sums π/2 = Σ k!/(2k+1)!! times 2S, so p ≈ πS (x is the current
  term, ratio i/(2i+1) with `i-~i` = 2i+1), and in the same pass counts the
  lattice points: A(n) = 1 + 4·Σ (⌊√(n − i²)⌋ + 1) over i = 1…⌊√n⌋. Past
  √n, `i*i<=n and` adds `False` and keeps `isqrt` away from negative
  numbers.
- Each floor loses less than 1 and earlier losses halve at every step, so
  0 ≤ πS − p < E = 2·log₂S + 6. The scale S = 9^⌊√n⌋ makes the series
  long enough to reach every column (the A000099 page has the bound).
- |P(n)| > |P(m)| is tested as |A·S − p·n| > |a·S − p·m|, the old record
  measured again with the new p; a = m = 0 makes n = 1 a record against 0.

**Why the precision is enough**

- Mahler (1953): |π − u/q| > q⁻⁴² for all integers u and q ≥ 2, so
  |qπ − u| > q⁻⁴¹; for q = 1, |π − u| > 1/8.
- ||P(n)| − |P(m)|| is |(A − a) − π(n − m)| or |(A + a) − π(n + m)|, with
  multipliers between 1 and 2n, so it exceeds (2n)⁻⁴¹, while the
  approximations move the two sides by less than 2n·E/S together. So the
  test is right whenever S ≥ E·(2n)⁴², which holds for every n ≥ 50 176
  (see [A000099](../A000099/)); below that the output was checked against
  the b-files.
- Ties |P(n)| = |P(m)| cannot happen for n ≠ m, since π is irrational.

**Notes**

- Records with equal A: a(5) = a(6) = 69 are A(20) and A(24), two records
  in a row of the same disc.
- `from math import*` pays for `isqrt` twice.
- Each n costs a fresh π to about 3.2·√n bits, so the program prints about
  55 terms (n ≈ 58 000, A ≈ 182 000) in a minute on a busy machine. The
  bar is 45 terms (A = 89653 at n = 28559); the b-file has 200 terms.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 177 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000323), CC BY-SA 4.0.
