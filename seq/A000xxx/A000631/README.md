# A000631

> Number of ethylene derivatives with n carbon atoms.
> — [OEIS A000631](https://oeis.org/A000631)

Offset 2: 1, 1, 3, 5, 13, 27, 66, 153, 377, 914, …

### Python 3 — 167 bytes

```python
from math import*
Q=G=1,;n=0
while[print(sumprod(G,G[::-1])+G[n]>>1)]:Q+=*[0]*5,(sumprod(Q[::6]*2,G[::-2]+Q[3*n::-3])+Q[2*n])//3;n+=1;G+=0,sumprod(Q,Q[::-1])+Q[3*n]>>1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6.
  G = S₂(B) = (B² + B(x²))/2 counts unordered pairs of radicals, so
  P = x·G counts a carbon carrying two radicals ([A000642](../A000642/) is its series).
- An ethylene derivative is a double bond C=C whose two carbons each carry
  an unordered pair of radicals, and the two ends may be swapped:
  **a(n) = [x^(n−2)] S₂(G) = [x^(n−2)] (G(x)² + G(x²))/2** (the cycle
  index of D₄ on the four positions, (p₁⁴ + 2p₁²p₂ + 3p₂² + 2p₄)/8).
- Newton's identity gives 3·S₃(B) = B·G + B·B(x²) + B(x³), so
  Bₙ₊₁ = (Σⱼ Bⱼ(gₙ₋ⱼ + [x^(n−j)]B(x²)) + [xⁿ]B(x³))/3 with gₖ = [xᵏ]G.
- `Q` holds B with five zeros between terms (Q[6e] = Bₑ): `Q[3*n]` and
  `Q[2*n]` are [xⁿ]B(x²) and [xⁿ]B(x³), and `sumprod(Q,Q[::-1])` is
  [xⁿ]B² (only multiples of 6 meet). `G` holds g with one zero between
  terms (G[2e] = gₑ), so `G[n]` is [xⁿ]G(x²) and `sumprod(G,G[::-1])` is
  [xⁿ]G².
- In the B update, `Q[::6]*2` against `G[::-2]+Q[3*n::-3]` does both
  convolutions in one dot product.
- Each round prints a(n+2) = ([xⁿ]G² + [xⁿ]G(x²))/2 in the loop header,
  appends Bₙ₊₁, advances n and appends gₙ = ([xⁿ]B² + [xⁿ]B(x²))/2.

**Notes**

- Exact integer arithmetic. Both halvings are exact because
  F(x)² ≡ F(x²) (mod 2) for every integer series, and the division by 3
  is exact because it is Newton's identity for an integer series.
- O(n) operations per term. Python's 4300-digit limit for printing
  integers would stop it near n ≈ 9500.
- The reference file has the 499 terms of the OEIS b-file;
  the bar is all 499 in 60 s (it prints them in under a second here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000631), CC BY-SA 4.0.
