# A001615

> Dedekind psi function: n * Product_{p|n, p prime} (1 + 1/p).
> — [OEIS A001615](https://oeis.org/A001615)

Offset 1: 1, 3, 4, 6, 6, 12, 8, 12, 12, 18, 12, 24, 14, 24, 24, 24, 18, 36, 20, 36, 32, …

### Python 3 — 83 bytes

```python
P=[];n=r=1
while[print(r)]:
 r=n=n+1
 for p in P:r+=r//p>>n%p*n
 if r==n:P+=n,;r+=1
```

**How it works**

- `P` is the list of primes below n. For each p in it that divides n,
  `r+=r//p` multiplies r by 1 + 1/p. The division is exact: at that point
  r = (n/Q)·Π(q + 1), where Q is the product of the primes q < p that
  divide n, and p still divides n/Q.
- For a p that does not divide n, `r//p>>n%p*n` shifts the quotient right
  by at least n bits, which leaves 0, since r ≤ ψ(n) ≤ σ(n) < 2ⁿ (ψ sums
  n/d over the squarefree divisors d, σ over all of them). So the line adds
  r//p exactly when p | n, one byte shorter than `r//p*(n%p<1)`.
- If no prime below n divides n, r is still n, so n is prime: it joins
  `P` and ψ(n) = n + 1. The loop condition prints ψ(n) before the next n.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Term n loops over the π(n) primes below it; the whole b-file (10000
  terms) prints in about 3 s here, and the bar is the whole b-file.
- Summing n/d over the squarefree divisors d of n, with
  `all(d%k**2for k in range(2,d))` as the test, is 92 bytes; the sum over
  divisors c of #{x < c : gcd(x, c, n/c) = 1} with `from math import*` is
  over 100.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 83 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001615), CC BY-SA 4.0.
