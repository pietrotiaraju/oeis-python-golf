# A001605

> Indices of prime Fibonacci numbers.
> — [OEIS A001605](https://oeis.org/A001605)

Offset 1: 3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137, 359, 431, 433, 449, 509, 569, …

### Python 3 — 100 bytes

```python
import math
n=3;a,b=2,3
while[all(a%d for d in range(2,math.isqrt(a)+1))and print(n)]:a,b=b,a+b;n+=1
```

Sibling: the Lucas version [A001606](../A001606/).

**How it works**

- (a, b) = (F(n), F(n + 1)) walks along the Fibonacci numbers with
  `a,b=b,a+b;n+=1`. It starts at n = 3, F(3) = 2: F(0) = 0 and
  F(1) = F(2) = 1 are not prime.
- Each F(n) is tested for primality by trial division by every d from 2 to
  ⌊√F(n)⌋ (`math.isqrt` is exact): F(n) ≥ 2 is prime exactly when none of
  them divides it. That is the definition itself, so the program is right
  for every n and rests on no theorem or conjecture.
- `and print(n)` prints n when the test passes; the list `[…]` is never
  empty, so the loop runs forever.

**Notes**

- Exact for every n.
- Trial division up to √F(n) ≈ 1.27ⁿ is the whole cost: a(11) = 47
  (F(47) = 2971215073) comes at once and F(73) costs about 10⁷ divisions
  (its smallest factor is 9375829), but a(12) = 83 needs the primality of
  F(83) ≈ 10¹⁷, about 3·10⁸ divisions: out of reach. The bar is 11 terms
  in 60 s.
- Only prime n (and n = 4) can give a prime F(n), and the prime factors of
  F(p) are ≡ ±1 (mod p) for p ≠ 5; trying only those divisors proves F(83)
  in a few seconds, for 12 terms, but costs about 25 bytes.
- The 11 terms fit in a table shorter than the program, so it needs a
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001605), CC BY-SA 4.0.
