# A000441

> a(n) = Sum_{k=1..n-1} k*sigma(k)*sigma(n-k).
> — [OEIS A000441](https://oeis.org/A000441)

Offset 1: 0, 1, 9, 34, 95, 210, 406, 740, 1161, 1920, …

### Python 3 — 82 bytes

```python
n=1
while 1:print(n**1*sum(k*(5*k*k+1-6*n)for k in range(1,n+1)if n%k<1)//24);n+=1
```

**How it works**

- Write σ_j(n) = Σ_(d divides n) dʲ; σ(n) in the definition is σ_1(n).
  The weighted convolution identity on the OEIS page is

  **24a(n) = n^1·((1−6n)σ_1(n) + 5σ_3(n)).**

- Both divisor sums use the same divisors. Combine their summands:
  (1−6n)k + 5k³ = k·(5k²+1−6n).
  This is exactly the expression in the comprehension; `n%k<1`
  selects k dividing n, including k=1 and k=n.
- The factor `n**1` is applied to the complete sum before `//24`.
  The identity guarantees that this numerator is divisible by 24;
  individual divisor contributions need not be divisible by 24.
- At n=1 the sole contribution is 5+1−6=0, so the loop
  prints the required leading zero. No empty-convolution case needs
  a separate branch.

**Notes**

- Exact integers, with no table of precomputed σ values or third-party
  number-theory package. Some summands are negative; cancellation in
  the full sum produces the nonnegative convolution count.
- Testing all k from 1 through n costs O(n) remainder tests per term
  and O(N²) through n=N, with a constant number of accumulator values.
  It avoids computing two divisor sums for each of n−1 convolution
  positions separately.
- [A000477](../A000477/) and
  [A000499](../A000499/) are the other weighted
  convolutions in this family; the outer power and the two
  coefficients are the only changes to the expression.
- The b-file has 1000 terms (indices 1 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000441), CC BY-SA 4.0.
