# A001587

> Generalized Euler numbers.
> — [OEIS A001587](https://oeis.org/A001587)

Offset 0: 2, 6, 46, 522, 7970, 152166, 3487246, 93241002, 2849229890, …

### Python 3 — 99 bytes

```python
q=[0];r=[2];k=-1
while[print(r[k])]:q,r=r,[s:=-4*q[0]]+[s:=s+3*x for x in r[:k-1:-1]+r[k::-1]];k-=1
```

**How it works**

- **The e.g.f.** The entry gives 2(sin 3x + cos 3x)/(2 cos 4x − 1).
  Since cos 6x = cos 2x·(2 cos 4x − 1) and
  (cos 3x − sin 3x)(cos 3x + sin 3x) = cos 6x, this is
  **2 cos 2x / (cos 3x − sin 3x)**.
- **The triangle.** This is the doubled-middle boustrophedon of the
  Springer numbers ([A001586](../A001586/)) with a weight and an input:
  row m has 2m + 1 entries, row 0 is [u₀], and row m + 1 is the
  partial sums of u_(m+1), 3x₁, 3x₂, …, where x₁, x₂, … is row m read
  backwards with its middle entry read twice. The answer is the middle
  of each row.
- **Why.** Split row m into two halves sharing the middle,
  β(m, t) = entry m − t and α(m, t) = entry m + t (0 ≤ t ≤ m). The rule
  reads β(m, t) = β(m, t+1) + 3α(m−1, t),
  α(m, t+1) = α(m, t) + 3β(m−1, t), β(m, m) = u_m, α(m, 0) = β(m, 0).
  With A(i, j) = α(i+j, i) and B(i, j) = β(i+j, j) these are
  A(i+1, j) − A(i, j+1) = 3B(j, i) and B(i+1, j) − B(i, j+1) = 3A(j, i)
  for all i, j ≥ 0, so the e.g.f.s satisfy
  (∂ₓ − ∂ᵧ)𝒜(x, y) = 3ℬ(y, x), (∂ₓ − ∂ᵧ)ℬ(x, y) = 3𝒜(y, x). On each
  line x + y = s this is an oscillator: 𝒜 = α(s)cos 3x + β(s)sin 3x,
  ℬ = β(s)cos 3y − α(s)sin 3y (both equations check by differentiating,
  and the recurrences fix every entry from the edges, so this is the
  only solution). The edges are ℬ(0, y) = U(y) = Σ u_m·yᵐ/m! and
  𝒜(0, y) = ℬ(y, 0), so α = β and α(y)(cos 3y − sin 3y) = U(y). The
  middles are 𝒜(0, y) = α(y): their e.g.f. is
  **U(y)/(cos 3y − sin 3y)**.
- **The input.** U = 2 cos 2y gives u = 2, 0, −8, 0, 32, 0, …, so
  u_(m+1) = −4·u_(m−1): the first entry of the row before. `q` keeps
  the previous row, and `q=[0]` stands for a row −1 with u₋₁ = 0, which
  makes u₁ = 0.
- **The slices.** With k = −m − 1, `r[k]` is the middle of row m,
  `r[:k-1:-1]` runs from the end of the row down to the middle and
  `r[k::-1]` from the middle down to the start.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (200 terms, up to a(199)) prints in about a tenth of
  a second; the program reaches a(1315) in about 2.5 s, where the next
  term passes Python's 4300-digit int-to-str limit and it stops with a
  ValueError.
- The bar is the whole b-file in 60 s.
- Two weighted Seidel triangles (the even part sec 6x·(cos x + cos 5x)
  as in [A000192](../../A000xxx/A000192/), the odd part
  sec 6x·(sin x + sin 5x)) also work, but need two lists and two inputs.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 99 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001587), CC BY-SA 4.0.
