# A001239

> Numbers that are the sum of 3 nonnegative cubes in more than 1 way.
> — [OEIS A001239](https://oeis.org/A001239)

Offset 1: 216, 251, 344, 729, 855, 1009, 1072, 1366, 1457, 1459, 1520, 1674, 1728, 1729, 1730, 1737, 1756, 1763, 1793, …

### Python 3 — 151 bytes

```python
m=0;k=1
while 1:L=sorted(a**3+b**3+c**3for c in range(k)for b in range(c+1)for a in range(b+1));[print(m:=x)for x,y in zip(L,L[1:])if m<x==y<k**3];k*=2
```

**How it works**

- Each pass lists every a³ + b³ + c³ with 0 ≤ a ≤ b ≤ c < k and sorts it.
  A number below k³ has all its representations in the list (c³ < k³), so
  a value below k³ that appears twice in a row has more than one.
- `m` is the last number printed: `m<x==y<k**3` prints each such number
  once and skips those an earlier pass printed. Then k doubles.

**Notes**

- The whole b-file (10000 terms, up to 698040) prints in under a second.
- [A001235](../A001235/) is the version with two positive cubes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 151 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001239), CC BY-SA 4.0.
