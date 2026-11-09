# A001192

> Number of full sets of size n.
> — [OEIS A001192](https://oeis.org/A001192)

Offset 0: 1, 1, 1, 2, 9, 88, 1802, 75598, 6421599, 1097780312, 376516036188, 258683018091900, 355735062429124915, 978786413996934006272, 5387230452634185460127166, 59308424712939278997978128490, …

### Python 3 — 108 bytes

```python
from math import*
L=[];n=0
while[print(abs(b:=0**n-sum(L[k]*comb(2**k-k,n-k)for k in range(n))))]:L+=b,;n+=1
```

**How it works**

- A set is full (transitive) when each element is also a subset.
  V. Jovovic's identity Σₙ a(n)·xⁿ/(1+x)^(2ⁿ) = 1 becomes, with
  x = y/(1−y), Σₙ a(n)·yⁿ·(1−y)^(2ⁿ−n) = 1.
- Proof of the identity: the coefficient of yᵐ counts, with sign
  (−1)^|U|, the pairs (T, U) of a full set T and a set U of subsets of T
  that are not elements of T, with |T ∪ U| = m. Then X = T ∪ U is a full
  set of size m, and the pairs that give X are those whose U is a set of
  elements of X lying in no element of X (T = X ∖ U is then full, and each
  element of U is a subset of T). A non-empty finite full set has such an
  element (one of largest rank), so the signs cancel unless X = ∅.
- Reading off yᵐ: Σₖ a(k)·(−1)^(m−k)·C(2ᵏ−k, m−k) = [m = 0]. The list holds
  b(k) = (−1)ᵏ·a(k), which takes the signs out of the sum:
  b(m) = 0^m − Σₖ₌₀ᵐ⁻¹ b(k)·C(2ᵏ−k, m−k), and a(m) = |b(m)|.
- `0**n` is 1 at n = 0 and 0 afterwards.

**Notes**

- Exact integers; the 51 terms of the b-file print at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001192), CC BY-SA 4.0.
