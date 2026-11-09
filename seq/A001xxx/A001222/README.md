# A001222

> Number of prime divisors of n counted with multiplicity (also called big omega of n, bigomega(n) or Omega(n)).
> — [OEIS A001222](https://oeis.org/A001222)

Offset 1: 0, 1, 1, 2, 1, 2, 1, 3, 2, 2, 1, 3, 1, 2, 2, 4, 1, 3, 1, 3, 2, 2, 1, 4, 2, 2, 3, 3, 1, 3, 1, 5, 2, 2, 2, 4, 1, …

### Python 3 — 78 bytes

```python
A=[0]
for x in A:print(x);n=len(A);A+=1+max(A[d]--~n%-~d*n for d in range(n)),
```

**How it works**

- Ω(n) is the length of the longest chain of divisors 1 = d₀ | d₁ | ⋯ | n
  with each step a proper divisor: each step adds at least one prime
  factor, and dividing out one prime at a time adds exactly one. So
  Ω(n) = 1 + max Ω(d) over the divisors d < n, and Ω(1) = 0.
- `A` holds Ω(1), Ω(2), … and the loop reads it while it grows, so
  `for x in A:` is an endless loop that prints each value once it is in
  place. With n = `len(A)` the next number is n + 1, and `A[d]` is
  Ω(d + 1).
- `A[d]--~n%-~d*n` is Ω(d+1) − ((n+1) mod (d+1))·n: a divisor keeps its
  value, a non-divisor drops below 0 (Ω(d+1) < d + 1 ≤ n), and d = 0 (the
  divisor 1, value 0) keeps the max at least 0.

**Notes**

- A term costs n steps; about 9400 terms in 30 s here. The b-file has
  100000 terms; the bar is 7000 in 60 s.
- [A001221](../A001221/) counts the distinct primes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001222), CC BY-SA 4.0.
