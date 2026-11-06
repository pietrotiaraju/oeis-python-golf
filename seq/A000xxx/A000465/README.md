# A000465

> Number of bipartite partitions of n white objects and 4 black ones.
> — [OEIS A000465](https://oeis.org/A000465)

Offset 0: 5, 12, 29, 57, 109, 189, 323, 522, 831, 1279, …

This is a multiset partition of n identical white objects and 4
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series followed by 4 short
recurrence filters and one polynomial convolution.

### Python 3 — 284 bytes

```python
from math import*
a=[1];n=0;F=[];Q=[[0]*k for k in range(1,5)]
while 1:
 t=a[-1]
 for L in Q:t+=L.pop(0);L+=[t]
 F+=[t];print(sum(x*y for x,y in zip([5,2,0,-3,-5,-1,0,3,1,-1],F[::-1])))
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
- A partition λ of the fixed black total 4 specifies m_j
  parts having j black objects. Thus the required series is
  P(x)·Σ_(λ partitions 4) 1/∏ⱼ D_(m_j)(x).
  Bringing that finite sum over the common denominator D_4
  gives P(x)N(x)/D_4(x), where N's coefficients are
  [5, 2, 0, −3, −5, −1, 0, 3, 1, −1] in ascending degree order.
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
  `L.pop(0)` retrieves z(n−k), and `L+=[t]` saves z(n).
  The queues start with zeros for negative indices, and are built
  separately so their mutations do not alias one another.
- After the 4 filters, F holds coefficients of P/D_4.
  `zip(N,F[::-1])` takes their short convolution with N; zip
  stops at the available coefficients when n is small, implicitly
  treating negative-index terms as zero.

- At n=0 no white objects occur, leaving exactly the ordinary
  partitions of 4: 5. This is N(0),
  so the initial coefficient is produced by the same filters and
  convolution as every later one.

**Notes**

- Exact integer recurrences throughout. The numerator coefficients
  come from a finite generating-function identity, rather than
  from storing initial terms of the answer.
- The queue lengths total 10; a and F grow by
  one entry per term. The pentagonal sum has O(√n) summands,
  while `F[::-1]` also copies the whole accumulated F each round.
  These operations, plus large-integer arithmetic, set the runtime.
- [A000412](../A000412/) uses the same partition stream
  with a different black total, filter count and numerator.
  Python 3.11+ eventually reaches its default 4300-digit output
  conversion limit; that interpreter limit is not a wrong term.
- The b-file has 5001 terms (indices 0 through 5000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 284 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000465), CC BY-SA 4.0.
