# A001408

> High temperature series for spin-1/2 Ising specific heat on 3-dimensional simple cubic lattice, divided by 3.
> — [OEIS A001408](https://oeis.org/A001408)

Offset 0: 1, 11, 188, 2992, 51708, 930436, 17127356, 320726028, 6086177116, 116714440696, …

With v = tanh K (K = J/kT), the specific heat per spin of the simple
cubic Ising model above the critical temperature has the expansion
C/(k K²) = 3 Σ a(n) v²ⁿ = 3 + 33v² + 564v⁴ + …. Since
ln Z/N = ln 2 + 3 ln cosh K + ln Λ(v), with Λ the even-subgraph series of
[A001393](../A001393/), this is C/(kK²) = ∂²_K(3 ln cosh K + ln Λ) with
∂_K = (1 − v²) ∂_v; for example ln Λ = 3v⁴ + 22v⁶ + … gives 3(1 − v²) +
(1 − v²)∂_v((1 − v²)(12v³ + …)) = 3 + 33v² + …, so a(1) = 11.

### Python 3 — 437 bytes

```python
t=4
while 1:
 X=8**t**3;Y=X**(2*t-8);M=X*Y;C=0
 for a in 1,-5,10,-10,5,-1:
  for B in range(t**3):L=B//t;B%=t;s=L*B*max(t-L-B,0);D=[1+2**k<<i for k,q in((1,L),(L,L*B),(L*B,s))for i in range(s)if i%q<q-k];E=len(D);w=[(1+X)**(E-d)*(1-X)**d for d in range(E+1)];c=[sum(0<g&e<e for e in D)for g in range(1<<s)];Z,U,W=[sum(w[d]*d**j<<j for d in c)>>s for j in(0,1,2)];C+=a*(W*Z-U*U)*pow(Z,-2,M)
  t-=1
 print(((C+Y*-~X//2)%M//Y-X//2)//3);t+=7
```

**How it works**

- Finite-lattice method, as in [A001393](../A001393/): for the boxes σ of
  l × m × k sites (free boundaries) with T − 5 ≤ l + m + k ≤ T, and
  u = T − (l + m + k), Σ (−1)ᵘC(5, u) ln Z̃(σ) ≡ ln Λ (mod v^{2T−5}),
  where Z̃(σ) is the even-subgraph polynomial of the box. The same weights
  sum the site counts lmk to 1 and the edge counts to 3 (fifth differences
  of polynomials of degree 5 and 4 in l + m + k), so with the full box
  partition functions Z(σ) = 2^{lmk} coshᴱK · Z̃(σ) the window sum is the
  whole per-spin ln Z/N = ln 2 + 3 ln cosh K + ln Λ, to the same order.
- Each ∂_K = (1 − v²)∂_v lowers the order of the error by one, so
  Σ (−1)ᵘC(5, u) ∂²_K ln Z(σ) ≡ C/(kK²) (mod v^{2T−7}); the loop takes
  T = n + 4 (`t` starts at 4 and `t+=7` after six `t-=1`) and reads the
  coefficient of v²ⁿ.
- ∂²_K ln Z(σ) is the variance of the energy e = Σ_edges σσ′ = E − 2d (d
  unequal edges) under the Boltzmann weights, which up to the common factor
  coshᴱK are (1+v)^{E−d}(1−v)^d (the list `w`). The variance of e is that of
  2d, so with S_j = Σ_configurations w[d]·(2d)ʲ (`d**j<<j`), j = 0, 1, 2,
  it is (S₂S₀ − S₁²)/S₀². Each S_j is 2^{lmk} times an integer polynomial
  (it is cosh^{−E}K ∂ʲ_K of 2^{lmk}coshᴱK·Z̃ up to terms in S₀, S₁), so the
  shifts `>>s` are exact, and Z = S₀ >> s = Z̃(σ) ≡ 1 is a unit for the
  power-of-two modulus.
- The boxes, edge masks `1+2**k<<i`, the test `0<g&e<e` for an edge joining
  unequal spins and the Kronecker substitution v ↦ X = 8^{t³} modulo
  M = X^{2n+1} are those of A001393; `c` lists d for all 2ˢ spin
  configurations once, and the three sums reuse it.
- Reading the coefficient: `(C+Y*-~X//2)%M//Y-X//2` (Y = X²ⁿ) rounds the
  symmetric residue to the top digit, which is the coefficient of v²ⁿ when
  every coefficient below it is at most X/4 in size. With A001393's torus
  bound |[vʲ] ln Λ| ≤ (6N)ʲ, N = (2n+3)³, the coefficients of C/(kK²) up to
  v²ⁿ are at most 3 + 4(2n+4)²(6N)^{2n+2}, far below X/4 = 2^{3(n+4)³−2}.
  The final `//3` is the division in the sequence's definition.

**Golf notes**

- The variance of 2d instead of E − 2d: `d**j<<j` is three bytes shorter than
  `(E-2*d)**j`, and the shift keeps every S_j a multiple of 2ˢ.
- Differentiating the full ln Z(σ) rather than ln Z̃(σ) makes the term
  3(1 − v²) from 3 ln cosh K come out of the window sum by itself.

**Notes**

- Every step is exact integer arithmetic and the truncation order is proved
  above, so the program is correct for every n. a(4) needs boxes up to
  l + m + k = 8 (2 × 3 × 3, 2¹⁸ configurations) and comes after about 28 s
  here; a(5) needs the 3 × 3 × 3 box (2²⁷ configurations) and is far out of
  reach.
- The b-file has 19 terms (a(0) to a(18), the terms of the entry); the bar
  is 5 terms (up to a(4)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 437 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001408), CC BY-SA 4.0.
