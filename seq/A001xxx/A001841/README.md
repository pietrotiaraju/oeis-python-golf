# A001841

> Related to Zarankiewicz's problem.
> — [OEIS A001841](https://oeis.org/A001841)

Offset 3: 3, 5, 10, 14, 21, 26, 36, 43, 55, 64, 78, 88, 105, 117, 136, 150, …

### Python 3 — 38 bytes

```python
n=3
while[print(n*(3*n-3>>1)//3)]:n+=1
```

**How it works**

- **Definition.** The OEIS title only says "related to Zarankiewicz's
  problem" (the terms come from R. K. Guy's 1967 table, divided by 2).
  This page follows Charles Greathouse's comment there: a(n) is the largest
  number of triangles in Kₙ when each edge may be used at most 3 times, the
  3-fold triple packing number D₃(n,3,2). It agrees with all 9998 terms of
  the b-file.
- **Upper bound.** A vertex has 3(n−1) edge uses and each triangle through
  it takes two, so it lies in at most ⌊3(n−1)/2⌋ triangles; each triangle
  has three vertices, so a(n) ≤ ⌊n/3·⌊3(n−1)/2⌋⌋.
- **The bound is attained for every n.** The λ-fold triple packing numbers
  were determined for all λ and n by Hanani (*Discrete Math.* 11 (1975)
  255–369; Schönheim 1966 for λ = 1), and for λ = 3 there is no exception:
  the only obstruction, a leftover of exactly one edge when λ(n−1) is even,
  cannot occur because 3·n(n−1)/2 is a multiple of 3. For odd n a 3-fold
  triple system uses every edge exactly three times. A random search here
  also found packings of the bound for every n from 3 to 16.
- **Golf.** `3*n-3>>1` is ⌊3(n−1)/2⌋, and `n*m//3` is ⌊n/3·m⌋. For odd n
  this is n(n−1)/2; no single quadratic floor matches every n.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 9998 terms (n = 3 to 10000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001841), CC BY-SA 4.0.
