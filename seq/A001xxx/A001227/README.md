# A001227

> Number of odd divisors of n.
> — [OEIS A001227](https://oeis.org/A001227)

Offset 1: 1, 1, 2, 1, 2, 2, 2, 1, 3, 2, 2, 2, 2, 2, 4, 1, 2, 3, 2, 2, 4, 2, 2, 2, 3, 2, 4, 2, 2, 4, 2, 1, 4, 2, 4, 3, 2, …

### Python 3 — 56 bytes

```python
n=1
while[print(sum(n%d<1for d in range(1,n+1,2)))]:n+=1
```

**How it works**

- Counts the divisors of n among 1, 3, 5, …, n.

**Notes**

- The whole b-file (10000 terms) prints in about 7 s here.
- The queue loop `r=[1]` / `for n in r:r+=n+1,;print(sum(n%d<1for d in
  r[::2]))` is 57 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001227), CC BY-SA 4.0.
