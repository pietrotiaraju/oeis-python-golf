# A001449

> Binomial coefficients binomial(5n,n).
> — [OEIS A001449](https://oeis.org/A001449)

Offset 0: 1, 5, 45, 455, 4845, 53130, 593775, 6724520, 76904685, 886163135, 10272278170, …

### Python 3 — 51 bytes

```python
import math
n=0
while[print(math.comb(5*n,n))]:n+=1
```

**How it works**

- `math.comb(5*n,n)` is C(5n, n) itself (exact integers); `import math` and
  `math.comb` once is a byte under `from math import*` and `comb`.

**Notes**

- The ratio C(5n, n)/C(5n−5, n−1) = 5(5n−1)(5n−2)(5n−3)(5n−4) /
  (8n(4n−1)(2n−1)(4n−3)) is much longer to write, and reading C(5n, n)
  off (2^5n + 1)^5n with shifts breaks at n = 0.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001449), CC BY-SA 4.0.
