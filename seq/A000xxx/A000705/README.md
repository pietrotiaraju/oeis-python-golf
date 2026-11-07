# A000705

> n-th superior highly composite number A002201(n) is product of first n terms of this sequence.
> — [OEIS A000705](https://oeis.org/A000705)

Offset 1: 2, 3, 2, 5, 2, 3, 7, 2, 11, 13, 2, 3, 5, 17, 19, 2, 23, 7, 29, 3, …

### Python 3 — 288 bytes

```python
from decimal import*
c=getcontext();m=1
while 1:
 K=sorted((c.ln(p)/(c.ln(j+1)-c.ln(j)),p)for p in range(2<<m)for j in range(1,3*m)if p*j**-~m//(j+1)**m==j>0<all(p%d for d in range(2,p)));t=min(b[0]-a[0]for a,b in zip(K,K[1:]))*10**c.prec>m**3<<9;m+=t;c.prec*=2-t
 for _,p in K*t:print(p)
```

**What is computed**

- For ε > 0 the superior highly composite number is N_ε = ∏ pᵉ with
  e = ⌊1/(p^ε − 1)⌋, the number of j ≥ 1 with p^ε < (j+1)/j. As ε
  decreases, the exponent of p goes from j−1 to j when ε passes
  ε(p,j) = ln(1+1/j)/ln p. So the terms are the primes p of all pairs
  (p prime, j ≥ 1) taken in decreasing order of ε(p,j), that is, in
  increasing order of x(p,j) = 1/ε = ln p / ln((j+1)/j) (the greedy
  of T. D. Noe's Mathematica program).

**How it works**

- **Bands, exactly.** The pairs with ⌊x⌋ = m are those with
  ((j+1)/j)ᵐ ≤ p < ((j+1)/j)ᵐ⁺¹, i.e. j ≤ p·jᵐ⁺¹/(j+1)ᵐ < j+1: one
  integer floor division, `p*j**-~m//(j+1)**m==j`. In band m,
  p < 2ᵐ⁺¹ (the ratio is at most 2) and j < (m+1)/ln 2 < 3m, so
  `range(2<<m)` and `range(1,3*m)` cover it (p = 0, 1 never pass).
  The chain `==j>0<all(…)` runs the trial division only for pairs
  already in the band.
- **Order inside a band, certified.** The keys x are computed in
  `decimal` as `c.ln(p)/(c.ln(j+1)-c.ln(j))` at P digits; Python
  documents `ln` as correctly rounded and the other operations round to
  nearest. The difference of logs loses at most a factor (j+1)·ln(j+1)
  of relative accuracy (ln(1+1/j) ≥ 1/(j+1)), so each key is within
  (m+1)(10(j+1)ln(j+1)+15)·10⁻ᴾ of the true x. When the smallest gap
  between consecutive sorted keys exceeds 512m³·10⁻ᴾ, which is more than
  twice that bound for every m (j+1 < 1.45m+2.45), the computed order is
  the true order and the band is printed.
- Otherwise the flag `t` is false: `K*t` prints nothing, `m+=t` keeps the
  band, and `c.prec*=2-t` doubles the precision before trying it again.
  Starting from `decimal`'s default 28 digits this never happened in
  the first 15 bands (their smallest gap is 3.7·10⁻⁷).
- Two equal keys would make it retry forever. Such a tie is exactly the
  case Ramanujan's claim "every ratio is a prime" excludes, and ruling it
  out is open (it would follow from the four exponentials conjecture);
  where it happened the sequence itself would not be defined.
- `min` needs two keys per band: band m holds (p,1) for every prime
  p ∈ [2ᵐ, 2ᵐ⁺¹), at least two of them for m ≥ 3 by Ramanujan's
  π(x) − π(x/2) ≥ 2 for x ≥ 11; bands 1 and 2 have 3 and 4 pairs.

**Notes**

- Band 15 (up to term 6737) is done in about 36 s and band 16 (past
  term 10000) in about 130 s: the trial division up to p dominates.
- The b-file has 10000 terms; the bar is 5000 terms in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 288 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000705), CC BY-SA 4.0.
