# A002012

> Number of rooted planar maps with three trivalent vertices and a root vertex of degree 2*n - 1.
> — [OEIS A002012](https://oeis.org/A002012)

Offset 0: 4, 32, 200, 1120, 5880, 29568, 144144, 686400, 3208920, 14780480, 67251184, …

### Python 3 — 53 bytes

```python
a=4;j=2
while[print(a)]:j+=2;a=a*4*(j+4)*~-j//(j*j-4)
```

**How it works**

- **Maps counted.** Rooted planar maps (loops and multiple edges allowed)
  with three trivalent vertices and a root vertex of odd valence. With
  offset 0 the data start at a(0) = 4, the maps with a root vertex of
  valence 1, so a(n) counts root valence 2n + 1: the name's 2n − 1 belongs
  to an index starting at 1. The program follows the data.
- **Formula.** Mathai and Rathie (J. Combin. Theory B, 1972, Eq. (22), as
  cited in the entry) give a(n) = 2(n+3)·(2n+2)!/(3·n!·(n+1)!). It agrees
  with the root-edge recursion of [A002006](../A002006/) (the counts
  T(2n+1, 3) there) as far as that was run, n ≤ 9.
- **Running ratio.** a(n)/a(n−1) = 2(n+3)(2n+1)/(n(n+2)). With j = 2n + 2
  the denominator is (j²−4)/4 and the numerator (j+4)(j−1), so
  a(n) = 4(j+4)(j−1)·a(n−1)/(j²−4): one `j*j-4` instead of two factors,
  and `~-j` for j − 1. j starts at 2 (n = 0) and grows by 2.
- **Exact.** 4(j+4)(j−1)·a(n−1) equals (j²−4)·a(n), so the floor division
  is exact.

**Notes**

- `import math` with `2*m*(m+2)*math.comb(2*m,m)//3`, m = n + 1, is
  64 bytes. a(n) has about 0.6·n digits; the b-file has the 23 terms of
  the entry (n = 0 to 22), and the bar is all of them in 60 s, which takes
  a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002012), CC BY-SA 4.0.
