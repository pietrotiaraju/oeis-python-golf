# A001451

> a(n) = (5*n)!/((3*n)!*n!*n!).
> — [OEIS A001451](https://oeis.org/A001451)

Offset 0: 1, 20, 1260, 100100, 8817900, 823727520, 79919739900, …

### Python 3 — 64 bytes

```python
from math import*
n=0
while[print(comb(5*n,n)*comb(4*n,n))]:n+=1
```

**How it works**

- The multinomial coefficient splits into two binomials: choose the first
  n of the 5n places, then n of the remaining 4n,
  C(5n, n)·C(4n, n) = (5n)!/(n!(4n)!) · (4n)!/(n!(3n)!) = (5n)!/((3n)! n! n!).
- `math.comb` is exact, so the program is right for every n; the loop prints
  in its condition (`[None]` is true) and steps n, as in
  [A000027](../../A000xxx/A000027/).

**Notes**

- `perm(5*n,2*n)//perm(n)**2` (`math.perm` with one argument is n!) is 2
  bytes longer, and `f=factorial` with `f(5*n)//f(3*n)//f(n)**2` longer still.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 64 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001451), CC BY-SA 4.0.
