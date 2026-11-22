# A002197

> Numerators of coefficients for numerical integration.
> — [OEIS A002197](https://oeis.org/A002197)

Offset 0: 1, 17, 367, 27859, 1295803, 5329242827, 25198857127, …

### Python 3 — 133 bytes

```python
from fractions import*
w=[]
while w:=[y:=Fraction(j:=1,16*len(w)+24)]+[y:=(j*j*x-y/4)/(j-~j)/(j:=j+1)/2for x in w]:print(y.numerator)
```

**How it works**

- **Definition used.** Salzer's mid-interval formula with central
  differences: ∫ f over [x₀ − h/2, x₀ + h/2] equals
  h·(f₀ + (1/24)δ²f₀ − (17/5760)δ⁴f₀ + (367/967680)δ⁶f₀ − …), and
  A002197/[A002198](../A002198/) are the numerators and denominators, in
  lowest terms, of the absolute values b(n) of the coefficient of
  δ^(2n+2). The entry gives no formula in this form, so the program
  derives one: in Stirling's central interpolation formula the term in
  δ^(2m)f₀ is t²·∏_(k<m) (t² − k²)/(2m)!, the odd terms vanish on the
  symmetric interval, and so
  b(n) = (2/(2n+2)!)·∫₀^(1/2) t²·∏_(k=1..n) (k² − t²) dt
  (every factor is positive there). This reproduces all 101 terms of both
  b-files, and agrees with the entry's generating function
  1/x − 1/(√x·arcsin √x), whose coefficient of xⁿ is 4^(n+1)·b(n).
- **Moments.** Put t = s/2: b(n) = ∫₀¹ s²·∏ (4k² − s²) ds /
  (4^(n+1)·(2n+2)!). With J_j(m) = ∫₀¹ s^(2m+2)·∏_(k≤j) (4k² − s²) ds,
  J₀(m) = 1/(2m + 3) and J_j(m) = 4j²·J_(j−1)(m) − J_(j−1)(m+1). Scaled,
  K_j(m) = J_j(m)/(4^(j+1)·(2j+2)!) satisfies
  K_j(m) = (j²·K_(j−1)(m) − K_(j−1)(m+1)/4)/((2j+1)(2j+2)), with
  K₀(m) = 1/(16m + 24), and b(n) = K_n(0).
- **Anti-diagonals.** As in [A002195](../A002195/): `w` holds the entries
  with j + m = L − 1; the next diagonal starts from the seed K₀(L) and
  builds K_j(L−j) from the entry just made (`y`, moment m + 1) and the old
  one (`x`, moment m); its last entry is b(L). Exact `Fraction`s, one term
  per pass, forever.
- **Golf.** `Fraction(j:=1,…)` resets the counter j, and
  `/(j-~j)/(j:=j+1)/2` divides by (2j+1), (j+1) and 2 while advancing j at
  its last use.

**Notes**

- The b-file has 101 terms (n = 0 to 100), and the bar is the whole b-file
  in 60 s, which takes a fraction of a second; the program prints about
  600 terms in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-22 | Python 3 | 133 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002197), CC BY-SA 4.0.
