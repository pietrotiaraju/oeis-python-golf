# A001897

> Denominators of cosecant numbers: -2*(2^(2*n-1)-1)*Bernoulli(2*n).
> — [OEIS A001897](https://oeis.org/A001897)

Offset 0: 1, 3, 15, 21, 15, 33, 1365, 3, 255, 399, 165, 69, 1365, 3, 435, 7161, 255, 3, …

### Python 3 — 79 bytes

```python
import math
n=1
while[print(math.gcd(*(k**n-k for k in range(n)))//2or 1)]:n+=2
```

**How it works**

- c(n) = −2(2^(2n−1) − 1)B(2n). By von Staudt–Clausen the denominator of B(2n) is the product of
  the primes p with (p − 1) | 2n, each once. The factor 2 cancels the prime 2, and no odd one of
  those primes divides 2^(2n−1) − 1: 2^(2n) ≡ 1 (mod p) by Fermat, so 2^(2n−1) ≡ 1/2 ≢ 1. So for
  n ≥ 1, a(n) = ∏ p over the odd primes p with (p − 1) | 2n, and a(0) = 1 (c(0) = 1).
- That product, times 2, is gcd(k^(m+1) − k : 0 ≤ k ≤ m) for m = 2n, with no prime test: in the
  program `n` is m + 1 and `range(n)` gives k = 0, …, m.
  - Every prime p with (p − 1) | m divides each k^(m+1) − k (Fermat), and p² does not divide them
    all: k = p gives p^(m+1) − p when p ≤ m, and the other case, p = m + 1, takes k = m = p − 1,
    with (p − 1)^p − (p − 1) ≡ −p (mod p²).
  - If p ≤ m + 1 divides them all, k runs over every residue mod p, so x^m ≡ 1 for all units and
    (p − 1) | m. A prime p ≥ m + 2 cannot divide them all: 1, …, m would be m distinct roots of
    x^m − 1 in 𝔽ₚ, hence all of them, and so a subgroup H of order m containing 2; then 2m mod p
    is in H = {1, …, m}, which forces p ≤ 2m, so |H| = m > (p − 1)/2 must be p − 1, against
    p ≥ m + 2.
- `//2` removes the prime 2. For n = 0 the range holds only k = 0, the gcd is 0, and `or 1`
  gives a(0) = 1.

**Notes**

- Exact integer arithmetic. The b-file has 52 terms (n ≤ 51); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001897), CC BY-SA 4.0.
