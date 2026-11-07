# A000598

> Number of rooted ternary trees with n nodes; number of n-carbon alkyl radicals C(n)H(2n+1) ignoring stereoisomers.
> — [OEIS A000598](https://oeis.org/A000598)

Offset 0: 1, 1, 1, 2, 4, 8, 17, 39, 89, 211, …

### Python 3 — 129 bytes

```python
from math import*
L=1,;n=0
while[print(L[-1])]:L+=sumprod(L,L[::-1])+3*L[3*n]>>1,;L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1
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
- Each round the loop header prints Bₙ = `L[-1]`, then Kₙ and Bₙ₊₁ are
  appended.

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
| 2026-11-06 | Python 3 | 189 | first entry |
| 2026-11-06 | Python 3 | 158 | use exact sumprod convolutions and compact coefficient initialization |
| 2026-11-07 | Python 3 | 129 | cache K = (B²+3B(x²))/2 and interleave B, K in one tuple |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000598), CC BY-SA 4.0.
