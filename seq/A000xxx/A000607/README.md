# A000607

> Number of partitions of n into prime parts.
> — [OEIS A000607](https://oeis.org/A000607)

Offset 0: 1, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 7, 9, 10, …

### Python 3 — 97 bytes

```python
a=[1];*P,F,n=1,0
while[print(a[-1])]:n-=1;P+=F%-n*[n];F*=n*n;a+=sum(d*sum(a[d::d])for d in P)//n,
```

**How it works**

- The generating function is ∏ 1/(1 − x^p) over the primes p. Its
  logarithmic derivative gives n·a(n) = Σₖ sopf(k)·a(n − k), where sopf(k) is
  the sum of the distinct primes dividing k ([A008472](https://oeis.org/A008472)).
  Grouped by prime: n·a(n) = Σ_{p ≤ n} p·Σ_{j ≥ 1} a(n − jp).
- As in the [A000041](../A000041/) record the counter runs downwards,
  n = −m. `P` holds the negated primes d = −p ≤ m, and `a[d::d]` starts at
  index m − p of the list a(0), …, a(m − 1) and steps back by p: exactly
  a(m − p), a(m − 2p), … . Each product d·Σ is negative, and `//n` with the
  negative n divides it exactly.
- Primes come from Wilson's theorem: F = ((m − 1)!)², so F mod m is 1 when m
  is prime and 0 otherwise (also for m = 1, and for m = 4 where F = 36).
  `F%-n*[n]` therefore appends −m to `P` exactly when m is prime, and then
  `F*=n*n` moves F on to (m!)².
- The starred assignment sets P = [], F = 1, n = 0.

**Notes**

- Exact integer arithmetic: the division by n is exact because the identity
  above is exact, and Wilson's theorem decides primality.
- F has about 2m·log₂m bits, small next to the O(m·π(m)) slice sums per term.
- The program printed 16888 to 18624 terms in 60 s in two runs on the
  reference PC. The bar is 13000 terms; the b-file has 50001 (n = 0 to 50000).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 97 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000607), CC BY-SA 4.0.
