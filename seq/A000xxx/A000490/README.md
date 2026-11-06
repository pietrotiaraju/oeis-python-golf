# A000490

> Generalized Euler numbers c(4,n).
> — [OEIS A000490](https://oeis.org/A000490)

Offset 0: 1, 16, 1280, 249856, 90767360, 52975108096, 45344872202240, 53515555843342336, 83285910482761809920, 165262072909347030040576, …

### Python 3 — 114 bytes

```python
import math
a=[1]
while[print(a[-1])]:
 n=len(a);a+=[-sum(math.comb(2*n,2*k)*(-16)**k*a[-k]for k in range(1,n+1))]
```

**How it works**

- Let F(x)=sec(4x)=Σₙ≥₀ a(n)x^(2n)/(2n)!. Since F is even, only
  the even derivatives are stored; the sequence index n corresponds to
  derivative order 2n, rather than n.
- The identity cos(4x)·F(x)=1 and the product rule give a(0)=1 and,
  for n≥1,

  **a(n)=−Σₖ₌₁ⁿ C(2n,2k)·(−16)ᵏ·a(n−k).**

  Here (−16)ᵏ is the 2k-th derivative of cos(4x) at zero. Its
  constant derivative is 1, so the k=0 term is precisely a(n).
- `a=[1]` seeds that constant coefficient. The loop prints the most
  recent entry first, then `n=len(a)` selects the next index and
  `a[-k]` supplies the coefficient n−k in the convolution.
- For example, a(1)=−(−16)=16, and
  a(2)=−(6·(−16)·16+256)=1280.

**Notes**

- Exact integers throughout: `sec` is a formal generating function,
  not a floating-point function evaluated by the program.
- Equivalently a(n)=16ⁿ·E(2n), where E(2n) are the positive secant
  numbers. Combining the scale into the convolution avoids computing
  the unscaled sequence and then multiplying each output separately.
- One list holds n+1 terms; computing the next one uses n+1 summands.
  [A000436](../A000436/) and [A000464](../A000464/) use the same
  denominator-convolution method with nonconstant numerators.
- Factorial growth eventually reaches Python 3.11+'s default
  4300-digit integer-to-string limit, which is an interpreter limit.
- The b-file has 195 terms (indices 0 through 194). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 115 | first entry |
| 2026-11-06 | Python 3 | 114 | use a shorter math import |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000490), CC BY-SA 4.0.
