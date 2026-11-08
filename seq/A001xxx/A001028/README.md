# A001028

> E.g.f. A(x) satisfies A'(x) = 1 + A(A(x)), with A(0) = 0.
> — [OEIS A001028](https://oeis.org/A001028)

Offset 1: 1, 1, 2, 7, 37, 269, 2535, 29738, 421790, 7076459, 138061343, …

### Python 3 — 153 bytes

```python
import math,functools
f=functools.cache(lambda n,k:k and sum(math.comb(n-1,j)*f(j,k+1)*f(n-j,k-1)for j in range(n))or n<2)
n=0
while 1:n+=1;print(f(n,1))
```

**Why it works**

- Let A^k be the k-th iterate of A (A^0(x) = x). By the chain rule and
  A′ = 1 + A∘A,

  (A^k)′ = A′(A^(k−1))·(A^(k−1))′ = (1 + A^(k+1))·(A^(k−1))′.

- Let f(n, k) = n!·[xⁿ](1 + A^k), so f(0, k) = 1 and f(n, k) is the
  e.g.f. coefficient of A^k for n ≥ 1. Taking (n−1)!·[x^(n−1)] of the
  product above:

  **f(n, k) = Σ_(j=0..n−1) C(n−1, j)·f(j, k+1)·f(n−j, k−1)**,

  which is Seiichi Manyama's recurrence in the entry with the "1 +" folded
  into f(0, ·). The base is f(n, 0) = n!·[xⁿ](1 + x): 1 for n ≤ 1, else 0.
- a(n) = f(n, 1), and every f(n, k) needs only smaller n or the same n
  with smaller k, so the recursion is well founded.

**How it works**

- `k and S or n<2`: for k ≥ 1 and n ≥ 1 the sum S is positive (iterates
  of a series with positive coefficients), so it is returned; for n = 0
  the sum is empty, 0, and the `or` gives the 1 (as `True`); for k = 0 it
  gives the base. `f(1,1)` comes out as the int 1 because the sum adds
  `True` to 0.
- `functools.cache` memoizes; `import math,functools` with both prefixes
  is 4 bytes under the two star imports.

**Notes**

- Exact integer arithmetic, correct for every n.
- The table has about n²/2 entries and n terms each: the whole b-file
  (320 terms) in about 25 s here, using about 40 MB, and nearly 400 terms
  in 60 s. The bar is 300 terms in 60 s.
- Each new term recurses about n levels deep (two frames per level, the
  lambda and its generator), so after 498 terms, about three minutes in,
  it stops with `RecursionError` at Python's default limit of 1000: an
  interpreter limit, far beyond the bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 153 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001028), CC BY-SA 4.0.
