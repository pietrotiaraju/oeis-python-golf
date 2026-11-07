# A000879

> Number of primes < prime(n)^2.
> — [OEIS A000879](https://oeis.org/A000879)

Offset 1: 2, 4, 9, 15, 30, 39, 61, 72, 99, 146, 162, 219, 263, 283, 329, 409, …

### Python 3 — 68 bytes

```python
P=k=1;S={0}
while 1:k in S==print(len(S)-1);S|={P%k*k*k};P*=k*k;k+=1
```

**How it works**

- a(n) = π(p_n²). The loop walks k = 1, 2, 3, … with `P` = ((k−1)!)², so by
  Wilson's theorem `P%k` is 1 when k is prime and 0 otherwise (also at k = 1
  and k = 4: 0!² mod 1 = 0, 3!² = 36 ≡ 0 mod 4).
- `S` collects `P%k*k*k`: k² for every prime k, and 0 for the others. It
  starts as `{0}`, so `len(S)-1` is the number of primes found so far.
- At each k, before k is added, `k in S==print(len(S)-1)` prints when k is
  the square of a prime p. Then the count is π(p² − 1) = π(p²), as p² is
  not prime. The chained comparison only calls `print` when `k in S`.
- Each prime p is added at k = p, long before k reaches p², and the squares
  come in increasing order, so the terms come out in order.
- Letting the set count the primes is 3 bytes under a separate counter
  (`c=0` and `c+=P%k`, printing `c`).

**Notes**

- Exact integer arithmetic; the only facts used are Wilson's theorem and
  that p² is composite.
- `P` has about 2k·log₂k bits and each step multiplies it and takes a
  remainder, so reaching k costs about k² operations: 62–66 terms in 60 s
  (up to p ≈ 300, k ≈ 10⁵).
- The b-file has 10000 terms; the bar is 48 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000879), CC BY-SA 4.0.
