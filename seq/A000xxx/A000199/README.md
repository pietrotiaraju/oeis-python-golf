# A000199

> Coefficient of q^(2n-1) in the series expansion of Ramanujan's mock theta function f(q).
> — [OEIS A000199](https://oeis.org/A000199)

Offset 1: 1, 3, 3, 7, 6, 12, 13, 20, 21, 34, 36, 51, 58, 78, 89, 118, …

### Python 3 — 106 bytes

```python
m=1
while r:=[1]*m:
 k=m
 while k:
  for j in range(k,m):r[j]-=r[j-k]
  k-=1;r=[-r[0]]+r
 print(r[m]);m+=2
```

**How it works**

- These are the odd-index coefficients of [A000025](../A000025/), f(q) =
  Σ q^(n²)/((1+q)²⋯(1+qⁿ)²). Instead of that sum the program uses Fine's
  form, which needs one division per level instead of two:

  f(q) = 1 − Σ_{n≥1} (−1)ⁿ qⁿ / ((1+q)(1+q²)⋯(1+qⁿ)).

  It follows from f(q) = Σ_λ (−1)^rank(λ) q^|λ| (the rank generating
  function at z = −1): partitions with largest part L give
  −q^L/((1+q)⋯(1+q^L)) when each part counts −1, times (−1)^L.
- In Horner form, with t = 1 at the bottom and k = m, …, 1,

  t ← (−1)^k + q · t / (1+q^k),

  ends at t = f − 2, so for m ≥ 1 the coefficient of qᵐ in t is the one in
  f. Moving the signs into the constants this way costs less than the
  `1 − q·t` of the plain Horner form, which has to negate the whole list.
- Dividing by 1 + q^k is `r[j]-=r[j-k]` for ascending j, and
  `r=[-r[0]]+r` multiplies by q and adds the next constant. The division
  never touches index 0, so `r[0]` is still the previous constant, and the
  constants alternate. m is odd, so the bottom constant (−1)^(m+1) is 1.
- An index j at level k ends up at j + k after the remaining shifts, so
  only j ≤ m − k matters there. The list starts with m entries and grows by
  one per level, so `range(k,m)` covers every index that reaches qᵐ, and
  `[1]*m` stands in for the bottom t = 1: only its constant term
  reaches qᵐ.

**Notes**

- Exact integer arithmetic, correct for every n. Each term is recomputed
  from scratch in about m² steps: 655 terms in 60 s on the test PC. The
  bar is 500 terms in 60 s; the b-file has 5000.
- Taking the A000025 program with m odd (`m=1`, `m+=2`) gives 118 bytes.
- Packing the series into one integer at q = −2^m, with the divisions done
  as `pow(1+(-2**m)**k,-1,M)`, is 99 bytes but decodes the digits as
  nonnegative. That needs the coefficients of f(q) to alternate in sign for
  every n, which follows from the Andrews–Dragonette asymptotics only for
  large n, and it prints just 79 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 106 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000199), CC BY-SA 4.0.
