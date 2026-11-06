# A000428

> Euler transform of A000579.
> — [OEIS A000428](https://oeis.org/A000428)

Offset 1: 1, 8, 36, 148, 554, 2094, 7624, 27428, 96231, 332159, …

The input weights are A000579, c(k) = C(k+5,6). The
program rearranges the Euler-transform divisor sums into a single
coefficient recurrence; it never expands the infinite product directly.

### Python 3 — 111 bytes

```python
from math import*
a=[1];n=0
while 1:n-=1;a+=sum(d*comb(5-d,6)*sum(a[d::d])for d in range(n,0))//n,;print(a[-1])
```

**How it works**

- The input weights are c(k)=C(k+5,6). The Euler transform
  has generating function A(x)=∏ₖ≥₁(1−xᵏ)^(−c(k)), with a(0)=1.
- Logarithmic differentiation gives
  m·a(m)=Σᵣ₌₁ᵐ b(r)a(m−r), where
  b(r)=Σ_(k divides r) k·c(k). Interchanging the finite sums gives

  **m·a(m)=Σₖ₌₁ᵐ k·c(k)·Σⱼ₌₁^⌊m/k⌋ a(m−jk)**.

- Before computing a(m), the list a contains a(0), …, a(m−1),
  and the code's n is −m. For d=−k, the slice `a[d::d]` is
  a(m−k), a(m−2k), …, stopping before the index becomes negative.
- `comb(5-d,6)` is c(k). Both d and n carry a minus sign,
  so their signs cancel in the exact division. Append the next
  coefficient and print it; no separate divisor-sum list is needed.
- The auxiliary a(0)=1 supplies the recurrence, while output starts
  at a(1), as required by the OEIS offset.

**Notes**

- Exact integer arithmetic follows from the formal Euler product.
  The sum rearrangement is finite at each coefficient and imposes
  no approximation or conjecture.
- One growing coefficient list is stored. The nested slice sums
  use O(m log m) entries for coefficient m, plus the cost of
  binomial coefficients and large-integer arithmetic.
- [A000417](../A000417/)
  uses the same method with a different binomial weight. This is
  the specified Euler transform, rather than a formula for actual
  partitions in that many dimensions.
- The b-file has 1000 terms. The unchanged bar is the whole
  reference file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |
| 2026-11-06 | Python 3 | 160 | use a shorter math import |
| 2026-11-06 | Python 3 | 111 | reorder the Euler-transform sum and use one coefficient list |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000428), CC BY-SA 4.0.
