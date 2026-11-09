# A001361

> Number of points in interior of n-th crystal ball in E_8 lattice.
> — [OEIS A001361](https://oeis.org/A001361)

Offset 1: 1, 241, 26641, 338401, 2240161, 10242001, 36638641, 109907521, …

### Python 3 — 81 bytes

```python
n=1
while[print(((((((19*n-17)*n+53)*n-115)*n-24)*n-108)*n-8)*n*~-n*3//7+1)]:n+=1
```

**How it works**

- The interior of the n-th crystal ball is the set of E₈ points at
  distance less than n from the origin in the contact graph, so a(n) is the
  sum of the coordination numbers S(0), …, S(n−1) of E₈. Their
  generating function (Conway and Sloane, *Low-Dimensional Lattices VII*,
  1997; the growth series of root lattices were proved by Bacher,
  de la Harpe and Venkov, 1997) has denominator (1 − x)⁸, so the entry's
  generating function x·N(x)/(1 − x)⁹, N of degree 8, makes a(n) a
  polynomial of degree 8 in n for every n ≥ 1.
- Interpolating it gives
  7·a(n) = 57n⁸ − 108n⁷ + 210n⁶ − 504n⁵ + 273n⁴ − 252n³ + 300n² + 24n + 7.
  The non-constant coefficients are all multiples of 3, and a(1) = 1
  makes n = 1 a root of 7·(a(n) − 1), so
  a(n) = 1 + 3n(n − 1)·R(n)/7 with
  R(n) = 19n⁶ − 17n⁵ + 53n⁴ − 115n³ − 24n² − 108n − 8,
  which the program evaluates by Horner's rule (`~-n` is n − 1).
  3n(n − 1)·R(n) = 7·(a(n) − 1) is a multiple of 7 for every integer n,
  so `//7` is exact.

**Notes**

- Horner on the full 7·a(n) is 87 bytes, and on 7·(a(n) − 1)/(3n) (no
  n − 1 factor) 84; nine running sums of the
  numerator coefficients, or the 9-term difference table, need longer
  literals.
- Exact integer arithmetic, so the program is right for every n ≥ 1.
- The b-file has 1000 terms (a(1) to a(1000)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001361), CC BY-SA 4.0.
