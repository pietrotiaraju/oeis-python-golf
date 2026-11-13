# A001562

> Numbers k such that (10^k + 1)/11 is a prime.
> — [OEIS A001562](https://oeis.org/A001562)

Offset 1: 5, 7, 19, 31, 53, 67, 293, 641, 2137, 3011, 268207, 1600787

### Python 3 — 120 bytes

```python
import math
k=P=1
while 1:P*=k*-~k;k+=2;N=10**k//11+1;P%k*all(N%d for d in range(2*k+1,math.isqrt(N)+1,2*k))and print(k)
```

**How it works**

- (10ᵏ + 1)/11 is an integer only for odd k (10 ≡ −1 (mod 11)), and then
  it equals ⌊10ᵏ/11⌋ + 1, which is `N`. k = 1 gives N = 1, so the scan
  runs over k = 3, 5, 7, …
- Odd composite k never give a prime: if q < k is an odd prime factor of k,
  then 10^q + 1 divides 10ᵏ + 1, so (10^q + 1)/11 is a factor of N strictly
  between 1 and N. Wilson's theorem skips those k: `P` is (k − 1)! (each
  pass multiplies it by (k − 2)(k − 1), written `k*-~k` before k grows by
  2), so `P%k` is k − 1 for a prime k and 0 for an odd composite one.
- For a prime k, every prime factor p of N other than 11 is ≡ 1 (mod 2k):
  10ᵏ ≡ −1 (mod p), so the order of 10 mod p divides 2k but not k, hence
  it is 2 or 2k. Order 2 means p | 99, and p = 3 never divides 10ᵏ + 1
  (≡ 2 (mod 3)), so p = 11; otherwise 2k | p − 1. And 11 divides N only
  when 121 | 10ᵏ + 1, that is (since 10ᵏ ≡ −1 + 11k (mod 121) for odd k)
  only when 11 | k, so only for k = 11, where N = 11·23·4093·8779 is caught
  by its factor 23 = 2·11 + 1 anyway.
- So for a prime k, N is composite exactly when it has a divisor d ≡ 1
  (mod 2k) with 2k + 1 ≤ d ≤ ⌊√N⌋ (its smallest prime factor), and
  `range(2*k+1,math.isqrt(N)+1,2*k)` tries exactly those d, with an exact
  integer square root. That is trial division with a step of 2k instead
  of 1: a proof of primality, not a probable-prime test.

**Notes**

- Exact for every n; it rests only on the facts above (Wilson's theorem,
  Fermat's little theorem through the order of 10).
- a(3) = 19 needs about 2.5·10⁷ trial divisions of the 18-digit N and
  arrives after about 5 s on the PC it was written on. a(4) = 31 would
  need about 1.5·10¹³ (N has 30 digits); the composite N for k = 23 and 29
  are dismissed at once by their factors 47 = 2·23 + 1 and 59 = 2·29 + 1.
  The bar is 3 terms in 60 s.
- The 3 terms fit in a table shorter than the program, so it needs a
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001562), CC BY-SA 4.0.
