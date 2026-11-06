# A000469

> 1 together with products of 2 or more distinct primes.
> — [OEIS A000469](https://oeis.org/A000469)

Offset 1: 1, 6, 10, 14, 15, 21, 22, 26, 30, 33, …

### Python 3 — 129 bytes

```python
from math import*
n=1
while 1:
 r=range(2,isqrt(n)+1)
 if all(n%(k*k)for k in r)and(n==1 or any(n%k<1 for k in r)):print(n)
 n+=1
```

**How it works**

- An integer is a product of distinct primes exactly when it is
  squarefree. A non-squarefree n has some prime-square divisor p²≤n,
  so it is enough to check square divisors k² for 2≤k≤⌊√n⌋.
- `all(n%(k*k)for k in r)` rejects any zero remainder, which
  detects every repeated prime factor. Composite k need not be
  omitted: their square divisors also imply a repeated prime factor.
- A squarefree positive integer is 1, a prime, or a product of at
  least two distinct primes. The second condition accepts 1 explicitly
  and otherwise requires a divisor in the same range, excluding primes.
- `r=range(2,isqrt(n)+1)` uses an exact square root and includes
  its upper endpoint. A range is reusable, so the second generator
  can traverse r again after `all` has traversed it.
- For n=1, `all` of the empty range is true and the explicit
  n==1 branch accepts it. For n=6 both tests pass; for n=12
  the square divisor 4 makes the first test fail.

**Notes**

- Exact divisibility tests; no probabilistic prime test or approximate
  square root is involved. The conditions characterize every integer
  in the definition, including its special initial 1.
- The generators short-circuit at a failed squarefree check or a found
  ordinary divisor. A candidate needs at most O(√n) trials in each
  pass, with constant auxiliary storage.
- [A000430](../A000430/) selects primes and prime squares, while
  this page rejects both of those types and keeps the squarefree
  composite products, together with 1.
- The b-file has 10000 terms (indices 1 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 129 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000469), CC BY-SA 4.0.
