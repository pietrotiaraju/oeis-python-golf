# A001358

> Semiprimes (or biprimes): products of two primes.
> — [OEIS A001358](https://oeis.org/A001358)

Offset 1: 4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, …

### Python 3 — 85 bytes

```python
S={n:=2}
while 1:
 n+=1;k=2
 while n%k:k+=k*k<n or n-k
 S|={k};n//k in S and print(n)
```

**How it works**

- **The test.** Let k be the smallest divisor of n above 1; it is a prime.
  n is a product of two primes if and only if n/k is a prime: if n = pq
  with p ≤ q, then k = p and n/k = q; if n has three or more prime factors,
  n/k still has two; and if n is prime, n/k = 1.
- **The smallest divisor.** The inner loop tries k = 2, 3, … while k does
  not divide n. Once k² ≥ n with no divisor found, n is prime, and
  `k+=k*k<n or n-k` jumps straight to k = n (it adds `True`, that is 1,
  while k² < n). A composite n has its smallest divisor at most √n, so the
  jump never skips it, and a prime costs only about √n steps.
- **The primes.** `S` holds every prime found so far: the loop leaves
  k = n exactly when n is prime, and otherwise k is a prime already in
  `S`, so `S|={k}` adds the new primes and nothing else. Since n/k < n,
  `n//k in S` decides whether n/k is prime; for a prime n it asks about 1,
  which is never in `S`.
- `S={n:=2}` starts with S = {2} and n = 2; the loop runs from n = 3.

**Notes**

- Integer arithmetic only, correct for every n; the work is about √n per
  prime and the smallest prime factor per composite.
- The bar is the whole b-file (20000 terms, up to 84829) in 60 s, which
  takes about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001358), CC BY-SA 4.0.
