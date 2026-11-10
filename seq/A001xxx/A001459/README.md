# A001459

> a(n) = (5*n)!/((2*n)!*(2*n)!*n!).
> — [OEIS A001459](https://oeis.org/A001459)

Offset 0: 1, 30, 3150, 420420, 62355150, 9816086280, 1605660228900, …

### Python 3 — 66 bytes

```python
from math import*
n=0
while[print(comb(5*n,n)*comb(4*n,2*n))]:n+=1
```

**How it works**

- The multinomial coefficient splits into two binomials: choose the n
  places of the single block among 5n, then 2n of the remaining 4n,
  C(5n, n)·C(4n, 2n) = (5n)!/(n!(4n)!) · (4n)!/((2n)!(2n)!) = (5n)!/((2n)!(2n)! n!).
- `math.comb` is exact, so the program is right for every n; the loop prints
  in its condition (`[None]` is true) and steps n, as in
  [A000027](../../A000xxx/A000027/).

**Notes**

- `comb(5*n,2*n)*comb(3*n,n)` is the same length; with `math.perm` (one
  argument gives n!), `perm(5*n,3*n)//perm(2*n)//perm(n)` is 8 bytes longer.
- The b-file has 401 terms (n = 0 to 400); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001459), CC BY-SA 4.0.
