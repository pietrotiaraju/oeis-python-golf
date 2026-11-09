# A001272

> Numbers k such that k! - (k-1)! + (k-2)! - (k-3)! + ... - (-1)^k*1! is prime.
> — [OEIS A001272](https://oeis.org/A001272)

Offset 1: 3, 4, 5, 6, 7, 8, 10, 15, 19, 41, 59, 61, 105, 160, 661, 2653, …

The alternating factorial af(k) = k! − (k−1)! + … ± 1!
([A005165](https://oeis.org/A005165)) satisfies af(k) = k! − af(k−1)
with af(0) = 0. The sequence is finite: 3612703 divides af(k) for every
k ≥ 3612702 (Živković, *Math. Comp.* 68 (1999), with H. Havermann's note on
the entry), so no term exceeds 3612701.

### Python 3 — 101 bytes

```python
from math import*
N=5;k=3
while[all(N%i for i in range(3,isqrt(N)+1,2))>0==print(k)]:k+=1;N=perm(k)-N
```

**How it works**

- `N` is af(k): it starts at af(3) = 6 − 2 + 1 = 5 and each step does
  `N=perm(k)-N`, that is af(k) = k! − af(k−1) (`perm(k)` is k!). The
  values for k = 1 and 2 are af(1) = af(2) = 1, not prime, so starting at
  k = 3 skips no term.
- af(k) is odd for k ≥ 1: af(1) = 1, and k! is even for k ≥ 2, so the
  parity never changes. So odd trial divisors 3, 5, …, ⌊√N⌋ decide
  primality exactly; `all(…)` is true exactly when N is prime (N ≥ 5).
- `all(…)>0==print(k)` is a chained comparison: k is printed only when
  af(k) is prime. The list around it is never empty, so the loop never
  stops by itself.
- Everything is exact, so every printed k is a term and none is skipped.
  The program keeps searching after the last term; past k = 3612701 it
  finds only multiples of 3612703.

**Notes**

- Trial division only works while af(k) is small. The 9th term needs
  af(19) = 115578717622022981, about 1.7·10⁸ odd divisors, which takes
  about 16 reference seconds. The next term, k = 41, has a 50-digit
  af(k) that no trial division can finish. Deterministic Miller–Rabin with
  the first 13 prime bases, proven below 3.3·10²⁴ (Sorenson and Webster
  2015), only covers k ≤ 24 and finds no term after 19 either. The OEIS
  data from k = 2653 on are probable primes.
- `range(2,isqrt(N)+1)` is 2 bytes shorter but tries twice as many
  divisors, over 30 reference seconds for af(19), too slow for the bar.
- The b-file is synthesized from the 25 terms of the entry (up to 59961);
  the bar is 9 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 101 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001272), CC BY-SA 4.0.
