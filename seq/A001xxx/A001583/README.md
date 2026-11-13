# A001583

> Artiads: the primes p == 1 (mod 5) for which Fibonacci((p-1)/5) is divisible by p.
> — [OEIS A001583](https://oeis.org/A001583)

Offset 1: 211, 281, 421, 461, 521, 691, 881, 991, 1031, 1151, 1511, 1601, 1871, 1951, 2221, 2591, 3001, 3251, 3571, 3851, …

### Python 3 — 107 bytes

```python
import math
p=b=1;a=0
while 1:p+=10;a+=b;b+=a;a%p or all(p%d for d in range(2,math.isqrt(p)+1))and print(p)
```

**How it works**

- An odd prime p ≡ 1 (mod 5) is ≡ 1 (mod 10), and 2 ≢ 1 (mod 5), so the
  scan p = 11, 21, 31, … misses nothing.
- k = (p − 1)/5 grows by 2 when p grows by 10, so the pair
  (a, b) = (F(k), F(k + 1)) takes two Fibonacci steps per pass:
  `a+=b;b+=a` gives (F(k + 2), F(k + 3)). It starts at (F(0), F(1)) = (0, 1)
  for p = 1, k = 0.
- The Fibonacci numbers are kept exact, so `a%p` is the divisibility test
  itself, with no modular doubling formulas.
- Only when p divides F(k) does trial division up to ⌊√p⌋ (exact
  `math.isqrt`) check that p is prime; composite p that pass the Fibonacci
  test are dropped there.

**Notes**

- Exact for every n.
- F(k) has about 0.14·p bits, so each pass costs time proportional to p
  and the run is quadratic: a(10000) = 2758631 arrives after about 21 s on
  the PC it was written on. The b-file has 24903 terms; the bar is 10000
  terms in 60 s.
- Fast doubling modulo p (log k steps per p) behind a base-2 Fermat
  filter does the whole b-file in about 13 s, but it is 188 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 107 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001583), CC BY-SA 4.0.
