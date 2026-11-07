# A000651

> Running time of Takeuchi function.
> — [OEIS A000651](https://oeis.org/A000651)

Offset 0: 0, 1, 4, 14, 53, 223, 1034, 5221, 28437, 165859, 1029803, 6772850, …

### Python 3 — 124 bytes

```python
from math import*
a=[n:=0]
while[print(a[n])]:a+=(105>>n%6*2&3)+a[n]+sum((-1)**k*comb(n-k,k+1)*a[~k]for k in range(n)),;n+=1
```

**How it works**

- Prellberg's functional equation (on the OEIS page) is
  A(z − z²)/z − A(z) = 1/(1 − z) + z/(1 − z + z²). The right side is
  1/((1 − z)(1 − z + z²)), whose coefficients gₙ are 1, 2, 2, 1, 0, 0
  repeating with period 6.
- [zⁿ] of A(z − z²)/z is Σₘ aₘ·[z^(n+1−m)](1 − z)ᵐ =
  Σₘ (−1)^(n+1−m)·C(m, n+1−m)·aₘ. The term m = n+1 is aₙ₊₁ itself, so
  aₙ₊₁ = gₙ + aₙ + Σ_{m≤n} (−1)^(n−m)·C(m, n+1−m)·aₘ.
- With m = n − k the sum is Σₖ (−1)ᵏ·C(n−k, k+1)·aₙ₋ₖ. The list holds
  a₀ … aₙ, so `a[~k]` (= `a[-k-1]`) is aₙ₋ₖ. The k = 0 term is n·aₙ;
  k = n would need C(0, n+1) = 0, so `range(n)` is enough.
- `105>>n%6*2&3` is gₙ: 105 = 1 + 2·4 + 2·4² + 1·4³ holds the period
  1, 2, 2, 1, 0, 0 as base-4 digits.

**Notes**

- Exact integer arithmetic, so the program is right for every n. All 571
  terms of the b-file print in a few seconds; Python's 4300-digit limit for
  printing ints stops it at a(1978), after about a minute.
- The PARI recurrence on the OEIS page, a Catalan sum plus ballot numbers
  `comb(n+k-1,k)*(n-k)//n` times earlier terms, is 130 bytes.
- The bar is the whole b-file, 571 terms, in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 124 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000651), CC BY-SA 4.0.
