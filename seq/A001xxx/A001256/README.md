# A001256

> Squares of numbers of trees.
> — [OEIS A001256](https://oeis.org/A001256)

Offset 0: 1, 1, 1, 1, 4, 9, 36, 121, 529, 2209, 11236, 55225, 303601, 1692601, 9979281, 59923081, 373262400, 2364779641, …

### Python 3 — 142 bytes

```python
F=1,;n=-1
while[print((F[n]+sum(F[i]*((i-~i==n)-F[n+~i])for i in range(n))//2)**2)]:n+=1;F+=sum(d*F[~d]*sum(F[d::d])for d in range(~n,0))//~n,
```

**How it works**

- The program is the [A000055](../../A000xxx/A000055/) record with its
  term squared. That record keeps the rooted trees in `F` (Euler
  transform), and Otter's formula (rooted trees minus pairs, plus the
  symmetric-edge term) gives the unrooted count.

**Notes**

- The whole b-file (1001 terms) prints in about a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 142 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001256), CC BY-SA 4.0.
