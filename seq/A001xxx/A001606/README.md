# A001606

> Indices of prime Lucas numbers.
> — [OEIS A001606](https://oeis.org/A001606)

Offset 1: 0, 2, 4, 5, 7, 8, 11, 13, 16, 17, 19, 31, 37, 41, 47, 53, 61, 71, 79, 113, …

### Python 3 — 105 bytes

```python
import math
n=0;a,b=2,1
while[a>1==all(a%d for d in range(2,math.isqrt(a)+1))and print(n)]:a,b=b,a+b;n+=1
```

Sibling: the Fibonacci version [A001605](../A001605/).

**How it works**

- (a, b) = (L(n), L(n + 1)) walks along the Lucas numbers 2, 1, 3, 4, 7,
  11, … with `a,b=b,a+b;n+=1`, from n = 0.
- Each L(n) is tested for primality by trial division by every d from 2 to
  ⌊√L(n)⌋ (`math.isqrt` is exact): L(n) ≥ 2 is prime exactly when none of
  them divides it. `a>1==all(…)` is "a > 1 and all(…)", which drops
  L(1) = 1. That is the definition itself, so the program is right for
  every n and rests on no theorem or conjecture.
- `and print(n)` prints n when the test passes; the list `[…]` is never
  empty, so the loop runs forever.

**Notes**

- Exact for every n.
- Trial division up to √L(n) ≈ 1.27ⁿ is the whole cost: a(18) = 71 needs
  about 2.6·10⁷ divisions to prove L(71) = 688846502588399 prime (about
  12 s on the PC it was written on), and a(19) = 79 about 1.3·10⁸. The bar
  is 18 terms in 60 s.
- Only n = 0, primes and powers of 2 can give a prime L(n), and for such
  n other than 0 and 3 every prime factor of L(n) is ≡ ±1 (mod 2n); trying
  only those divisors reaches a(19) = 79 but costs about 45 bytes.
- The 18 terms fit in a table shorter than the program, so it needs a
  review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 105 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001606), CC BY-SA 4.0.
