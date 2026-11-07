# A000763

> Number of interval orders constructed from n intervals of generic lengths.
> — [OEIS A000763](https://oeis.org/A000763)

Offset 1: 1, 3, 19, 195, 2831, 53703, 1264467, 35661979, 1173865927, 44218244943, …

### Python 3 — 178 bytes

```python
from math import*
c=lambda u,v:sum(comb(n,k)*u[k]*v[~k]for k in range(n+1))
Q=[];Y=A=[1];n=0
while 1:Q+=c(Y,Y),;Y=Y+[(4*(n+3)*c(Q,Y)-3*(n+2)*Q[n])//6];A+=c(Q,A),;n+=1;print(A[n])
```

**How it works**

- The OEIS e.g.f. E(x) satisfies E′/E = y², where y(2 − e^(xy)) = 1.
- An ODE for y: differentiating e^(xy) = 2 − 1/y gives
  (2 − 1/y)(y + xy′) = y′/y², i.e. y′ = y²(2y−1) + x·y(2y−1)·y′, and
  y(2y−1)y′ = (2y³/3 − y²/2)′. Comparing coefficients of xⁿ:
  6(n+1)·[xⁿ⁺¹]y = 4(n+3)·[xⁿ]y³ − 3(n+2)·[xⁿ]y².
- The program works with e.g.f. coefficients (n! times the ordinary ones),
  which are all integers here: Y for y, Q for y², A for E. Products are
  binomial convolutions, `c(u,v)` = Σₖ C(n,k)·uₖ·v_{n−k} at the current n
  (`v[~k]` is v[n−k] because v has exactly n+1 entries when it is called).
- Each round: Qₙ = c(Y,Y); the y³ coefficient is c(Q,Y), so
  6Y_{n+1} = 4(n+3)·c(Q,Y) − 3(n+2)·Qₙ; and E′ = E·y² gives
  A_{n+1} = c(Q,A) = a(n+1), which is printed.
- `Y=A=[1]` starts both lists as one object: `Y=Y+[…]` rebinds Y to a new
  list, so `A+=` grows the old one alone (2 bytes under two lists).

**Notes**

- Exact integer arithmetic, no fractions; the division by 6 is exact
  because Y has integer coefficients (y = φ(z) with φ the e.g.f. of
  [A000670](../A000670/) and z the reversion of z(2 − e^z)).
- Three convolutions per term; the whole b-file (100 terms) prints in a
  fraction of a second, and it is the bar.
- Lagrange inversion also gives log E directly: its e.g.f. coefficients
  are 2F(n+1, n−1)/(n+1) with F(r,m) = m!·[tᵐ](2 − eᵗ)^(−r), which satisfies
  F(r, m+1) = r(2F(r+1, m) − F(r, m)). Building F per term and then
  exponentiating was 192 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 178 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000763), CC BY-SA 4.0.
