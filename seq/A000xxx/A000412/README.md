# A000412

> Number of bipartite partitions of n white objects and 3 black ones.
> — [OEIS A000412](https://oeis.org/A000412)

Offset 0: 3, 7, 16, 31, 57, 97, 162, 257, 401, 608, …

This is a multiset partition of n identical white objects and 3
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series followed by 3 short
recurrence filters and one polynomial convolution.

### Python 3 — 261 bytes

```python
from math import*
a=[1];n=0;F=[0]*6;Q=[[0]*k for k in range(1,4)]
while 1:
 t=a[-1]
 for L in Q:L+=[t:=t+L.pop(0)]
 F=[t]+F;print(sumprod([3,1,-1,-2,-1,1],F[:6]))
 n+=1;a+=[sum((k%2*2-1)*a[-k*(3*k-1)//2]for k in range(-isqrt(n),isqrt(n)+1)if 0<k*(3*k-1)//2<=n)]
```

**How it works**

- A part is a pair (i,j) of nonnegative counts, not both zero:
  i white objects and j black objects. Parts are unordered and may
  repeat. The bivariate generating function is therefore
  ∏_((i,j)≠(0,0)) (1−xⁱyʲ)⁻¹.
- Parts with j=0 give the ordinary partition series
  P(x)=∏ᵢ≥₁(1−xⁱ)⁻¹. For a fixed positive black count j,
  Euler's q-binomial identity gives
  ∏ᵢ≥₀(1−yʲxⁱ)⁻¹=Σₘ≥₀ y^(jm)/D_m(x), with
  D_m(x)=∏ₖ₌₁ᵐ(1−xᵏ) and D_0(x)=1.
- A partition λ of the fixed black total 3 specifies m_j
  parts having j black objects. Thus the required series is
  P(x)·Σ_(λ partitions 3) 1/∏ⱼ D_(m_j)(x).
  Bringing that finite sum over the common denominator D_3
  gives P(x)N(x)/D_3(x), where N's coefficients are
  [3, 1, −1, −2, −1, 1] in ascending degree order.
- `a` stores ordinary partition numbers p(0), …, p(n), beginning
  with p(0)=1. The final line appends p(n+1) by Euler's pentagonal
  recurrence. The signed index k supplies the generalized
  pentagonal numbers k(3k−1)/2, and `k%2*2-1` supplies their
  alternating signs for positive and negative k alike.
- After `n+=1`, the range −⌊√n⌋≤k≤⌊√n⌋ contains every
  needed pentagonal index; the `if` removes k=0 and indices
  greater than n. Before the append the list has length n,
  so `a[-g]` is p(n−g).
- Each queue L of length k applies division by 1−xᵏ to the
  current coefficient stream: z(n)=input(n)+z(n−k).
  `L.pop(0)` retrieves z(n−k); the assignment expression adds
  it to t and `L+=[t:=t+L.pop(0)]` saves the new z(n).
  The queues start with zeros for negative indices, and are built
  separately so their mutations do not alias one another.
- After the 3 filters, t is the current coefficient of P/D_3.
  `F=[t]+F` puts it at the front of the history. The initial
  6 zeros supply coefficients at negative indices, so `F[:6]`
  always has exactly as many entries as the numerator polynomial.
  `sumprod` takes their exact integer dot product.

- For example the three black partitions 3, 2+1 and 1+1+1
  give 1/D_1+1/D_1²+1/D_3. Their common numerator is
  (1−x²)(1−x³)+(1+x)(1−x³)+1
  =3+x−x²−2x³−x⁴+x⁵, deriving the six stored constants.

**Notes**

- Exact integer recurrences throughout. The numerator coefficients
  come from a finite generating-function identity, rather than
  from storing initial terms of the answer.
- The queue lengths total 6; a and F grow by
  one entry per term. The pentagonal sum has O(√n) summands,
  while prepending to F also copies its accumulated history each round.
  These operations, plus large-integer arithmetic, set the runtime.
- [A000465](../A000465/) uses the same partition stream
  with a different black total, filter count and numerator.
  Python 3.11+ eventually reaches its default 4300-digit output
  conversion limit; that interpreter limit is not a wrong term.
- The b-file has 10001 terms (indices 0 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 275 | first entry |
| 2026-11-06 | Python 3 | 261 | use sumprod on padded coefficient history and combine queue updates |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000412), CC BY-SA 4.0.
