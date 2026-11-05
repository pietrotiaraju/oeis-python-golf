# A000169

> Number of labeled rooted trees with n nodes: n^(n-1).
> — [OEIS A000169](https://oeis.org/A000169)

Offset 1: 1, 2, 9, 64, 625, 7776, 117649, 2097152, 43046721, 1000000000, …

### Python 3 — 29 bytes

```python
n=1
while[print(n**~-n)]:n+=1
```

**How it works**

- Cayley's formula: there are n^(n−1) labeled rooted trees on n nodes.
  `~-n` is n−1 without parentheses, so `n**~-n` is n^(n−1).
- `n**n//n` is a byte longer.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (100 terms) prints at once; the program stops after a(1371), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000169), CC BY-SA 4.0.
