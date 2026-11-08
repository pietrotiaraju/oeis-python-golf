# A001066

> Dimensions (sorted, with duplicates removed) of real simple Lie algebras.
> — [OEIS A001066](https://oeis.org/A001066)

Offset 1: 3, 6, 8, 10, 14, 15, 16, 20, 21, 24, 28, 30, 35, 36, 42, 45, 48, 52, 55, 56, …

### Python 3 — 128 bytes

```python
import math
n=2
while[(0in(math.isqrt(x)**2-x for x in(n+1,2*n+4,8*n+1,4*n-~(n<13)))or{n,n/2}&{14,52,133,248})and print(n)]:n+=1
```

**How it works**

- **Which dimensions.** A real simple Lie algebra is either a real form of
  a complex simple algebra g (same dimension, dim g) or a complex simple g
  seen as a real algebra (dimension 2·dim g). So the terms are the numbers
  d and 2d for d in the complex list [A003038](https://oeis.org/A003038):
  Aₖ: k(k+2) for k ≥ 1, Bₖ and Cₖ: k(2k+1), Dₖ: k(2k−1), and G₂, F₄, E₆,
  E₇, E₈ = 14, 52, 78, 133, 248.
- **The classical series as square tests.** k(k+2) = j² − 1 with j = k+1,
  so d is in Aₖ iff d+1 is a square (d ≥ 3). k(2k+1) and k(2k−1) are the
  triangular numbers T₂ₖ and T₂ₖ₋₁, and Bₖ (k ≥ 2), Cₖ (k ≥ 3), Dₖ (k ≥ 4)
  together with A₃ = 15 cover every T_m with m ≥ 4, and n is triangular
  iff 8n+1 is a square. Doubling: n = 2(j²−1) iff 2n+4 = (2j)², and
  n = 2T_m = m(m+1) iff 4n+1 = (2m+1)².
- So n is a term iff one of n+1, 2n+4, 8n+1, 4n+1 is a perfect square, or n
  is 14, 52, 133, 248 or twice one of them, with three small corrections:
  n = 1 (8n+1 = 9, T₁) is skipped by starting at n = 2, and n = 2 and 12
  (4n+1 = 9 and 49, twice T₁ and T₃) are not terms, so `4*n-~(n<13)` adds
  1 below 13, where 4n+2 is never a square. The square tests catch
  T₂ = 3 and T₃ = 6 too, but those are terms anyway (3 = A₁, 6 = 2·A₁).
  E₆ = 78 = T₁₂ and 2·248 = 496 = T₃₁ need no entry of their own.
- `0in(math.isqrt(x)**2-x for …)` is the square test (isqrt(x)² − x is 0
  exactly for squares); `{n,n/2}&{…}` checks n and n/2 against the
  exceptional dimensions at once (n/2 is a float, equal to an int only
  for even n). `import math` with `math.isqrt` once is 1 byte under
  `from math import*`.

**Notes**

- Exact integer arithmetic (`n/2` only meets four small integers).
- The b-file has 10000 terms (up to 5918520); they print in about 25 s, and
  the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001066), CC BY-SA 4.0.
