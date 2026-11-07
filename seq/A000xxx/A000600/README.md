# A000600

> Number of tertiary alcohols (alkanols or alkyl alcohols C_n H_{2n+1} OH) with n carbon atoms.
> — [OEIS A000600](https://oeis.org/A000600)

Offset 0: 0, 0, 0, 0, 1, 1, 3, 7, 17, 40, …

### Python 3 — 145 bytes

```python
from math import*
L=1,;g=1;n=0
while[print(L[-1]-g)]:L+=(g:=sumprod(L,L[::-1])+L[3*n]>>1)+L[3*n],;L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1
```

**How it works**

- Let B(x) count alkyl radicals, with B₀ = 1 for a hydrogen. Pólya's S₃
  cycle index gives B = 1 + x·S₃(B), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6.
  Write S₂(F) = (F(x)² + F(x²))/2.
- Cache K = (B² + 3B(x²))/2 instead of B²: then B·K + B(x³) = 3·S₃(B), so
  Bₙ₊₁ = ([xⁿ]B·K + [xⁿ]B(x³))/3 needs one convolution once K is known,
  and Kₙ itself needs only [xⁿ]B².
- One tuple `L` interleaves both series: L[6e] = Bₑ, L[6e+1] = Kₑ, zeros
  elsewhere. `L[3*n]` and `L[2*n]` are [xⁿ]B(x²) and [xⁿ]B(x³) (those
  indices never land on a K slot), and `sumprod(L,L[::-1])` adds L[i]·L[j]
  over i + j = len(L) − 1: when L ends with Bₙ it is [xⁿ]B² (a K slot
  would need a partner in the empty slot 5), and right after Kₙ is
  appended it is 2[xⁿ]B·K. So one dot product serves both convolutions,
  and Bₙ₊₁ = (2[xⁿ]B·K + 2[xⁿ]B(x³))/6 is appended after four zeros.
- A tertiary carbon carries three nonempty radicals:
  a(n+1) = [xⁿ](S₃(B) − S₂(B)) = Bₙ₊₁ − gₙ, a(0) = 0, with
  gₙ = [xⁿ]S₂(B) = ([xⁿ]B² + [xⁿ]B(x²))/2 kept by the walrus (so
  Kₙ = gₙ + [xⁿ]B(x²)). The loop header prints Bₙ − g with g from the
  previous round; starting with g = 1 gives a(0) = B₀ − 1 = 0.

**Notes**

- Exact integer arithmetic: B² ≡ B(x²) (mod 2) makes the halving exact,
  and the division by 6 returns the integer Bₙ₊₁ = [xⁿ]S₃(B). There is no
  stereochemical distinction, matching the OEIS definitions.
- O(n) operations per term; Python's 4300-digit limit for printing
  integers would stop it near n ≈ 9500.
- The reference file contains 1001 terms from the OEIS b-file; the verification
  bar is 1001 terms in 60 s (the program needs about 2 s here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 226 | first entry |
| 2026-11-06 | Python 3 | 195 | use exact sumprod convolutions and compact coefficient initialization |
| 2026-11-07 | Python 3 | 145 | cache K = (B²+3B(x²))/2 and interleave B, K in one tuple |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000600), CC BY-SA 4.0.
