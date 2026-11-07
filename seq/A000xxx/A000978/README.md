# A000978

> Wagstaff numbers: numbers k such that (2^k + 1)/3 is prime.
> — [OEIS A000978](https://oeis.org/A000978)

Offset 1: 3, 5, 7, 11, 13, 17, 19, 23, 31, 43, 61, 79, 101, 127, 167, 191, 199, 313, 347, 701, …

### Python 3 — 66 bytes

```python
k=3
while[-1in(2**k%~d for d in range(3,1<<k//2))or print(k)]:k+=2
```

**How it works**

- k runs over the odd numbers from 3: for even k, 2^k + 1 is not divisible
  by 3, and k = 1 gives 1. W = (2^k+1)/3.
- `2**k%~d` is −1 exactly when d+1 divides 2^k+1 (`~d` is −(d+1), and the
  remainder takes the sign of the divisor), so the test looks for a divisor
  of 2^k+1 = 3W in 4 … 2^((k−1)/2).
- If W is prime, the divisors of 3W are 1, 3, W, 3W, and W > 2^((k−1)/2)
  for k ≥ 5, so none is found (for k = 3 the range is empty).
- If W is composite, its smallest factor a is odd and a ≤ √W < 2^((k−1)/2),
  since W < 2^(k−1). If a ≥ 4, a is found. If a = 3, then 9 divides 2^k+1,
  which happens only for k ≡ 3 (mod 6), so k ≥ 9 and 9 ≤ 2^((k−1)/2) is
  found.

**Notes**

- This is trial division up to √W: correct for every k, with no
  probable-prime test (the OEIS terms from a(32) on are only probable
  primes).
- 10 terms in about 1 s. The 11th, k = 61, needs 2³⁰ trial divisions, and
  k = 79 about 2³⁹; the bar is 10 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000978), CC BY-SA 4.0.
