# A000642

> a(n) = number of isomeric hydrocarbons of the acetylene series with carbon content n.
> — [OEIS A000642](https://oeis.org/A000642)

Offset 1: 0, 1, 1, 2, 3, 7, 14, 32, 72, 171, …

### Python 3 — 137 bytes

```python
from math import*
L=1,;g=n=0
while[print(g)]:L+=(g:=sumprod(L,L[::-1])+L[3*n]>>1)+L[3*n],;L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6. An
  acetylene R–C≡C–R′ is an unordered pair of radicals on the two triple-
  bonded carbons, so with G = S₂(B) = (B² + B(x²))/2:
  **a(n) = [x^(n−2)] G** for n ≥ 2, and a(1) = 0.
- With K = G + B(x²) = (B² + 3B(x²))/2 one has B·K + B(x³) = 3·S₃(B), so
  Bₙ₊₁ = ([xⁿ]B·K + [xⁿ]B(x³))/3.
- One tuple `L` interleaves both series: L[6e] = Bₑ, L[6e+1] = Kₑ, zeros
  elsewhere. `L[3*n]` and `L[2*n]` are [xⁿ]B(x²) and [xⁿ]B(x³) (those
  indices never land on a K slot), and `sumprod(L,L[::-1])` adds L[i]·L[j]
  over i + j = len(L) − 1: when L ends with Bₙ it is [xⁿ]B² (a K slot
  would need a partner in the empty slot 5), and right after Kₙ is
  appended it is 2[xⁿ]B·K. So one dot product serves both convolutions,
  and Bₙ₊₁ = (2[xⁿ]B·K + 2[xⁿ]B(x³))/6 is appended after four zeros.
- Each round the walrus computes gₙ = ([xⁿ]B² + [xⁿ]B(x²))/2, L gets
  Kₙ = gₙ + [xⁿ]B(x²) and then Bₙ₊₁. The loop header prints the previous
  g, which starts at 0 = a(1).

**Notes**

- Exact integer arithmetic: B² ≡ B(x²) (mod 2) makes the halving exact,
  and the division by 6 returns the integer Bₙ₊₁ = [xⁿ]S₃(B).
- O(n) operations per term. Python's 4300-digit limit for printing
  integers would stop it near n ≈ 9500.
- The reference file has the 201 terms of the OEIS b-file;
  the bar is all 201 in 60 s (it prints them in well under a second here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 137 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000642), CC BY-SA 4.0.
