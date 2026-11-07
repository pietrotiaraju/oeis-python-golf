# A000668

> Mersenne primes (primes of the form 2^n - 1).
> — [OEIS A000668](https://oeis.org/A000668)

Offset 1: 3, 7, 31, 127, 8191, 131071, 524287, 2147483647, 2305843009213693951, …

### Python 3 — 66 bytes

```python
k=s=0;m=3
while[s or print(m)]:k+=1;m-=~m;s=4;exec('s=s*s%m-2;'*k)
```

**How it works**

- The Lucas–Lehmer test, as in [A000043](../A000043/): with s₀ = 4 and
  sᵢ₊₁ = sᵢ² − 2, M = 2ⁿ − 1 (n ≥ 3) is prime exactly when M divides sₙ₋₂.
- Here the loop keeps M itself: `m-=~m` is m = 2m + 1, so after k passes
  m = 2^(k+2) − 1 and n − 2 = k is the number of steps in
  `'s=s*s%m-2;'*k`. Writing `~-(4<<k)` for M in both the print and the
  exec string instead, as A000043 does once, is 70 bytes.
- `s*s%m-2` keeps s in −2 … m − 3, where 0 is the only multiple of m, so
  `s or print(m)` prints m exactly when the test passes.
- n = 2 (M = 3) is the case the test misses; `k=s=0;m=3` makes the first
  loop condition see s = 0 and print 3 before any test runs.
- Every n is tested, prime or not. A composite n can never pass: if M
  divides sₙ₋₂ and q is the smallest prime factor of M, then
  ω = 2 + √3 has order 2ⁿ modulo q, so q² > 2ⁿ > M and M is prime (the
  argument is spelled out on the A000043 page).

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The bar is small because the terms grow fast: testing n costs n − 2
  squarings modulo an n-bit number, for every n. 2¹²⁷⁹ − 1 (the 15th term,
  386 digits) prints after about 16 s on the test machine, 2²²⁰³ − 1 takes
  more than a minute, and the b-file's 18 terms end with 2³²¹⁷ − 1. The bar
  is 15 terms in 60 s.
- From 2¹⁹⁹³⁷ − 1 on (more than 4300 digits) Python's int-to-string limit
  would stop the printing, long after the exec string (about 11·n bytes)
  and the running time have become the real limits.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000668), CC BY-SA 4.0.
