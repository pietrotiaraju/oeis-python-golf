# A001460

> a(n) = (5*n)!/((2*n)!*(n!)^3).
> — [OEIS A001460](https://oeis.org/A001460)

Offset 0: 1, 60, 18900, 8408400, 4364860500, 2473653742560, …

### Python 3 — 66 bytes

```python
from math import*
n=0
while[print(perm(5*n,3*n)//perm(n)**3)]:n+=1
```

**How it works**

- `math.perm(5*n,3*n)` is the falling factorial (5n)!/(2n)!, and `math.perm`
  with a single argument is n!, so the quotient is (5n)!/((2n)! (n!)³).
  The division is exact (it is a multinomial coefficient) and all the
  arithmetic is in integers, so the program is right for every n.
- The loop prints in its condition (`[None]` is true) and steps n, as in
  [A000027](../../A000xxx/A000027/).

**Notes**

- As binomials the term is C(5n, n)·C(4n, n)·C(3n, n);
  `prod(comb(k*n,n)for k in b'…')` (with the raw bytes 3, 4, 5) is 73 bytes,
  and `c=comb` + `c(5*n,n)*c(4*n,n)*c(3*n,n)` 74.
- The b-file has 401 terms (n = 0 to 400); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001460), CC BY-SA 4.0.
