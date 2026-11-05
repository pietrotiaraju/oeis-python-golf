# A000099

> Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi*n, P(n) = A(n) - V(n);
> sequence gives values of n where |P(n)| sets a new record.
> — [OEIS A000099](https://oeis.org/A000099)

Offset 1: 1, 2, 5, 10, 20, 24, 26, 41, 53, 130, 149, 205, 234, 287, 340, …

### Python 3 — 177 bytes

```python
from math import*
n=a=m=0
while S:=9**isqrt(n:=n+1):
 x=p=2*S;i=A=1
 while x:x=x*i//(i-~i);p+=x;A+=i*i<=n and 4+4*isqrt(n-i*i);i+=1
 if abs(A*S-p*n)>abs(a*S-p*m):a=A;print(m:=n)
```

**How it works**

- One loop does two jobs. It sums π/2 = Σ k!/(2k+1)!! = 1 + 1/3 +
  1·2/(3·5) + … times 2S, so p ≈ πS: x is the current term (ratio
  i/(2i+1), with `i-~i` = 2i+1) and p the running sum. Each floor loses
  less than 1 and the earlier losses halve at every step, so
  0 ≤ πS − p < E = 2·log₂S + 6.
- In the same pass it counts the lattice points:
  A(n) = 1 + 4·Σ (⌊√(n − i²)⌋ + 1) over i = 1…⌊√n⌋. Column i of the
  quarter i ≥ 1, j ≥ 0 holds ⌊√(n − i²)⌋ + 1 points, and four rotations
  of that quarter plus the origin make the whole disc. Past √n,
  `i*i<=n and` adds `False` (0) and keeps `isqrt` away from negative
  numbers.
- The scale S = 9^⌊√n⌋ makes the series long enough to reach every
  column. The loop runs while x > 0, and x_i > t_i − 2 where
  t_i = 2S·i!/(2i+1)!! ≥ 2S/(2^i·√(2i+1)); that is above 3 for every
  i < ⌊√n⌋, so i gets to ⌊√n⌋ before x hits 0.
- The record is kept as the pair (a, m) = (A(m), m), and |P(n)| > |P(m)|
  is tested as |A·S − p·n| > |a·S − p·m|, so the old record is measured
  again with the new p. a = m = 0 makes n = 1 a record against 0.

**Why the precision is enough**

- Mahler (1953): |π − u/q| > q⁻⁴² for all integers u and q ≥ 2, so
  |qπ − u| > q⁻⁴¹. For q = 1, |π − u| > 1/8.
- ||P(n)| − |P(m)|| is |P(n) − P(m)| or |P(n) + P(m)|, that is
  |(A − a) − π(n − m)| or |(A + a) − π(n + m)|. Both multipliers are
  between 1 and 2n, so the gap is more than (2n)⁻⁴¹. The two
  approximations move |P(n)| and |P(m)| by less than (n + m)·E/S < 2n·E/S
  together, so the test is right whenever S ≥ E·(2n)⁴².
- With S = 9^k, k = ⌊√n⌋, this holds for every k ≥ 224, that is every
  n ≥ 50 176 (checked in exact integers at the worst n = (k+1)² − 1 of
  each k up to 5000; beyond that 9^k only pulls further ahead of a
  polynomial in k). Below that, and in fact up to n = 114 243 (67 terms),
  the program's output was checked against the b-file.

**Notes**

- Same quantities as [A000036](../A000036/), which prints round(P(n)) at
  these n. A direct port of its program (separate `sum` for A(n),
  S = n⁴⁸) is 189 bytes; counting the columns inside the π loop saves 11.
- Each n costs a fresh π to about 3.2·√n bits, so the program prints
  about 67 terms (n ≈ 114 000) in a minute. The bar is 50 terms
  (n = 38 016) in 60 s; the b-file's 200 terms go up to n = 19 368 712.
- Floats are not enough: telling which of two n has the larger |P| needs
  π to more digits as n grows, and how many is what Mahler's bound pins
  down.
- The 178-byte version began its `while 1:` body with `n+=1;S=9**isqrt(n);`.
  Naming the value in the loop condition is 1 byte shorter and keeps the
  loop going, because S is a positive power of 9, and `n:=n+1` moves into
  it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 178 | first entry |
| 2026-11-05 | Python 3 | 177 | value named in the while condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000099), CC BY-SA 4.0.
