# A000632

> Number of esters with n carbon atoms up to structural isomerism.
> — [OEIS A000632](https://oeis.org/A000632)

Offset 2: 1, 2, 4, 9, 20, 45, 105, 249, 599, 1463, …

### Python 3 — 138 bytes

```python
from math import*
L=1,2;n=0
while 1:L+=*[0]*4,(sumprod(L,L[::-1])+2*L[2*n])//6;n+=1;L+=(c:=sumprod(L,L[::-1]))+3*L[3*n]>>1,;print(c-L[-2])
```

**How it works**

- B(x) = 1 + x·S₃(B) counts alkyl radicals with B₀ = 1 for a hydrogen
  ([A000598](../A000598/)), S₃(F) = (F(x)³ + 3F(x)F(x²) + 2F(x³))/6. An
  ester R–CO–O–R′ has the carbonyl carbon, a radical R (possibly H) and a
  nonempty radical R′, so **a(n) = [x^(n−1)] B(B − 1)**, the entry's
  formula.
- With K = (B² + 3B(x²))/2 one has B·K + B(x³) = 3·S₃(B), so
  Bₙ₊₁ = ([xⁿ]B·K + [xⁿ]B(x³))/3.
- One tuple `L` interleaves both series: L[6e] = Bₑ, L[6e+1] = Kₑ, zeros
  elsewhere. `L[3*n]` and `L[2*n]` are [xⁿ]B(x²) and [xⁿ]B(x³) (those
  indices never land on a K slot), and `sumprod(L,L[::-1])` adds L[i]·L[j]
  over i + j = len(L) − 1: when L ends with Bₙ it is [xⁿ]B² (a K slot
  would need a partner in the empty slot 5), and right after Kₙ is
  appended it is 2[xⁿ]B·K. So one dot product serves both convolutions,
  and Bₙ₊₁ = (2[xⁿ]B·K + 2[xⁿ]B(x³))/6 is appended after four zeros.
- `L=1,2` starts one step ahead with B₀ = 1, K₀ = 2. Each round appends
  Bₙ₊₁, advances n, computes c = [xⁿ]B², appends Kₙ = (c + 3[xⁿ]B(x²))/2
  and prints c − Bₙ (now `L[-2]`) = [xⁿ](B² − B) = a(n+1), starting with
  a(2).

**Notes**

- Exact integer arithmetic: B² ≡ B(x²) (mod 2) makes the halving exact,
  and the division by 6 returns the integer Bₙ₊₁ = [xⁿ]S₃(B).
- O(n) operations per term. Python's 4300-digit limit for printing
  integers would stop it near n ≈ 9500.
- The reference file has the 98 terms of the OEIS b-file;
  the bar is all 98 in 60 s (it prints them in well under a second here).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 138 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000632), CC BY-SA 4.0.
