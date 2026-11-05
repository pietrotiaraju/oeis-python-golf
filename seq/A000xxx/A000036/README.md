# A000036

> Let A(n) = #{(i,j): i^2 + j^2 <= n}, V(n) = Pi*n, P(n) = A(n) - V(n);
> A000099 gives values of n where |P(n)| sets a new record; sequence gives
> closest integer to P(A000099(n)).
> — [OEIS A000036](https://oeis.org/A000036)

Offset 1: 2, 3, 5, 6, 6, −6, 7, 8, 10, 13, 13, 13, 14, −17, 17, 17, 18, …

### Python 3 — 205 bytes

```python
from math import*
n=a=m=0
while 1:
 n+=1;S=6*n**47;x=p=2*S;i=1;A=1+4*sum(isqrt(n-i*i)for i in range(isqrt(n)+1))
 while x:x=x*i//(i-~i);p+=x;i+=1
 if abs(F:=A*S-p*n)>abs(a*S-p*m):a=A;m=n;print((F+S//2)//S)
```

**How it works**

- A(n) = 1 + 4·Σ ⌊√(n − i²)⌋ over i = 0…⌊√n⌋. The points with i ≥ 1,
  j ≥ 0 number Σ (⌊√(n − i²)⌋ + 1) over i = 1…⌊√n⌋, and the i = 0 term
  ⌊√n⌋ supplies the +1s. Four rotations of that quarter plus the origin
  make the whole disc.
- π is recomputed in integers for every n, at scale S = 6n⁴⁷. The inner
  loop sums π/2 = Σ k!/(2k+1)!! = 1 + 1/3 + 1·2/(3·5) + … times 2S: x is
  the current term (ratio i/(2i+1), with `i-~i` = 2i+1) and p the running
  sum. Each floor loses less than 1 and the earlier losses halve at every
  step, so 0 ≤ πS − p < E = 2·log₂S + 6.
- `F` = A·S − p·n is S·P(n), off by less than n·E. The record is kept as
  the pair (a, m) = (A(m), m), and |P(n)| > |P(m)| is tested as
  |F| > |a·S − p·m|, so the old record is measured again with the new p.
- The term is round(P(n)) = ⌊F/S + ½⌋ = `(F+S//2)//S` (S is even).
- a = m = 0 makes n = 1 a record against 0.

**Why the precision is enough**

- Mahler (1953): |π − u/q| > q⁻⁴² for all integers u and q ≥ 2, so
  |qπ − u| > q⁻⁴¹. For q = 1, |π − u| > 1/8.
- Record test: ||P(n)| − |P(m)|| is |P(n) − P(m)| or |P(n) + P(m)|, that
  is |(A − a) − π(n − m)| or |(A + a) − π(n + m)|. Both multipliers are
  below 2n, so the gap is more than (2n)⁻⁴¹. The two approximations move
  |P(n)| and |P(m)| by less than 2n·E/S together.
- Rounding: it can only go wrong if 2πn is within 2n·E/S of an odd
  integer, and |2πn − u| > (2n)⁻⁴¹.
- Both are safe when S ≥ E·(2n)⁴², that is 6n⁵ ≥ 2⁴²·E, which holds for
  every n ≥ 1000. Below that (the first 22 records), and in fact up to
  n = 201 600 (76 terms), the record positions the program finds were
  checked against [A000099](https://oeis.org/A000099) and the values against
  the b-file.

**Notes**

- Each n costs a fresh π to about 47·log₂n bits (≈ 0.24 ms at n = 10⁵)
  plus √n `isqrt` calls (≈ 0.02 ms), so the program prints about 70 terms
  (n ≈ 190 000) in a minute. The bar is 50 terms (n = 38 016) in 60 s; the
  b-file's 200 terms go up to n = 19 368 712.
- Floats are not enough: telling which of two n has the larger |P| needs
  π to more digits as n grows, and how many is exactly what Mahler's bound
  pins down. A fixed π would fail for some large n.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 205 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000036), CC BY-SA 4.0.
