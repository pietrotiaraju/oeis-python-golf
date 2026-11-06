# A000417

> Euler transform of A000389.
> — [OEIS A000417](https://oeis.org/A000417)

Offset 1: 1, 7, 28, 105, 357, 1232, 4067, 13301, 42357, 132845, …

The input weights are A000389, c(k) = C(k+4,5). The
program computes their Euler transform by a divisor sum followed by a
convolution; it never expands the infinite product directly.

### Python 3 — 160 bytes

```python
import math
a=[1];b=[0]
while 1:
 n=len(a);b+=[sum(k*math.comb(k+4,5)for k in range(1,n+1)if n%k<1)]
 a+=[sum(b[k]*a[n-k]for k in range(1,n+1))//n];print(a[-1])
```

**How it works**

- Put c(k) = C(k+4,5). The Euler transform has ordinary
  generating function A(x) = ∏ₖ≥₁ (1−xᵏ)^(−c(k)), with a(0) = 1.
  A factor chooses a multiset of parts of size k, in c(k) colors.
- Taking a formal logarithmic derivative gives
  xA′(x)/A(x) = Σₘ≥₁ b(m)xᵐ, where
  b(m) = Σ_(d divides m) d·c(d). Multiplying back by A yields
  **m·a(m) = Σₖ₌₁ᵐ b(k)·a(m−k)**.
- `n=len(a)` is the next index. The first comprehension computes b(n):
  `n%k<1` selects divisors and `k*comb(k+4,5)` is k·c(k).
  `b=[0]` keeps list positions aligned with those positive indices.
- Append b(n) before computing a(n), since the convolution includes
  b(n)·a(0). Append a(n) before printing `a[-1]`; the auxiliary a(0)=1
  is retained for the recurrence but the OEIS output starts at n=1.
- At n=2, b(1)=1 and b(2)=13, so
  a(2)=(1+13)/2=7, matching the second term.

**Notes**

- Every division by n is exact: A is an integer-coefficient Euler
  product. The calculation uses integers throughout, with no numeric
  approximation to an infinite product.
- Two lists hold n+1 coefficients. Finding b(n) tries n candidate
  divisors, and the second sum has n terms, so producing N terms takes
  O(N²) summands, apart from the cost of large-integer arithmetic.
- Compare [A000428](../A000428/): only the binomial weights
  change. The product here is the specified Euler transform; it does
  not enumerate actual partitions in that many dimensions.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |
| 2026-11-06 | Python 3 | 160 | use a shorter math import |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000417), CC BY-SA 4.0.
