# A000961

> Powers of primes. Alternatively, 1 and the prime powers (p^k, p prime, k >= 1).
> — [OEIS A000961](https://oeis.org/A000961)

Offset 1: 1, 2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27, 29, 31, 32, 37, …

### Python 3 — 65 bytes

```python
import math
L=m=1
while[L%m<1<m or print(m)]:L=math.lcm(L,m);m+=1
```

**How it works**

- `L` is lcm(1, …, m−1). A number m > 1 is a prime power p^k exactly when
  m does not divide `L`: the largest power of p in L is the largest one
  below m, and any other m is the product of prime powers that are smaller
  than m.
- `L%m<1<m` is false when m ∤ L, and also at m = 1, so `or print(m)`
  prints 1 and the prime powers.

**Notes**

- `import math` plus `math.lcm` is 1 byte under `from math import*`.
- The whole b-file (10000 terms) in about 8 s; the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 65 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000961), CC BY-SA 4.0.
