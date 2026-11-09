# A001275

> Smallest prime p such that the product of q/(q-1) over the primes from prime(n) to p is greater than 2.
> — [OEIS A001275](https://oeis.org/A001275)

Offset 1: 3, 7, 23, 61, 127, 199, 337, 479, 677, 937, 1193, 1511, 1871, …

The product runs over all primes q with prime(n) ≤ q ≤ p. A perfect or
abundant number whose smallest prime factor is prime(n) must have a prime
factor at least a(n). [A001276](../A001276/) counts the primes in the
product.

### Python 3 — 136 bytes

```python
P=[];N=m=r=1;D=2
while 1:
 m+=1;r+=r*r<=m
 if all(m%d for d in range(2,r)):P+=m,;N*=m;D*=m-1
 while N>D:print(m);N//=P[0];D//=P.pop(0)-1
```

**How it works**

- A sliding window of consecutive primes, kept as exact integers: `P`
  lists the primes from prime(n) up to the last prime found, `N` is their
  product and `D` is twice the product of the q − 1. So the product of
  q/(q − 1) over the window exceeds 2 exactly when `N>D`; no fractions or
  floats are needed.
- `m` runs over 2, 3, 4, … and is prime when no d with 2 ≤ d < r divides
  it. `r` keeps r² > m: when m grows by 1 with r² ≤ m, then r² = m and
  r grows to r + 1, whose square exceeds m. Since r ≤ √m + 1 < m from
  m = 3 on, the range covers every d ≤ √m and never m itself. Each prime
  m joins the window (`P+=m,;N*=m;D*=m-1`).
- After each prime the inner loop prints the answers it now has: while the
  window exceeds 2, its last prime m is a(n); then prime(n) leaves the
  window (`N//=P[0];D//=P.pop(0)-1`, both exact) and the test is repeated
  for n + 1 with the same m.
- This prints the smallest such prime. For n = 1 the window grows one
  prime at a time from 2 (2/1 = 2 is not greater than 2; with 3 it is 3).
  For n > 1, every window from prime(n) to a prime q < a(n − 1) has a
  product below that of the window from prime(n − 1) to q, which is at
  most 2; so starting the search at a(n − 1), which the window already
  ends at, misses nothing. The window never empties: a single factor
  q/(q − 1) is at most 2, so a(n − 1) ≥ prime(n).

**Notes**

- `N` is about the product of all primes up to m, about 1.44·m bits, so
  each new prime costs time proportional to m and the run is roughly
  quadratic: a(175) = 1144271 arrives after about 13 reference seconds,
  and about 210 terms within the 30 that count. Starting a new product
  for every n instead of sliding the window is far slower.
- a(n) = prime(n)² + o(prime(n)²) (the OEIS formula), so the window
  ends near prime(n)².
- The b-file has 650 terms (up to 23970113); the bar is 175 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 136 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001275), CC BY-SA 4.0.
