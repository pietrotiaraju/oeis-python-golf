# A000979

> Wagstaff primes: primes of form (2^p + 1)/3.
> — [OEIS A000979](https://oeis.org/A000979)

Offset 1: 3, 11, 43, 683, 2731, 43691, 174763, 2796203, 715827883, 2932031007403, 768614336404564651, …

### Python 3 — 68 bytes

```python
N=3;b=2
while[all(N%d for d in range(2,b))and print(N)]:N=4*N-1;b*=2
```

**How it works**

- N runs over (2^k+1)/3 for odd k = 3, 5, 7, …: going from k to k+2 is
  N → 4N − 1. b = 2^((k−1)/2) doubles at the same time.
- N is tested by trial division by 2 … b−1. Since N < 2^(k−1) = b², every
  composite N has a factor ≤ √N < b; and b ≤ N, so N itself is never tried.
- The OEIS name asks for prime p, but nothing is lost by trying every odd k:
  if k is composite with smallest prime factor a, then 2^a+1 divides 2^k+1,
  so N is divisible by 3 (a = 3, then N > 3) or by (2^a+1)/3 > 1 (a > 3), and
  is composite. For even k, (2^k+1)/3 is not an integer.

**Notes**

- Exact trial division up to √N, correct for every term; no probable-prime
  test is used.
- 10 terms in under 1 s. The 11th, 768614336404564651, needs about 2³⁰
  trial divisions; the bar is 10 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000979), CC BY-SA 4.0.
