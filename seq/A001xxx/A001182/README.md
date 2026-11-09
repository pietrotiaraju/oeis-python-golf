# A001182

> Number of cells of square lattice of edge 1/n inside quadrant of unit circle centered at 0.
> — [OEIS A001182](https://oeis.org/A001182)

Offset 1: 0, 1, 4, 8, 15, 22, 30, 41, 54, 69, 83, 98, 119, 139, 162, 183, …

### Python 3 — 79 bytes

```python
from math import*
n=1
while[print(sum(isqrt(n*n-i*i)-1for i in range(n)))]:n+=1
```

**How it works**

- Scale by n: the cells are the unit squares [i−1, i] × [j−1, j] with
  1 ≤ i, j ≤ n, and the quadrant is the quarter disc x² + y² ≤ n². A cell
  lies inside exactly when its far corner (i, j) does, so
  a(n) = #{(i, j) ≥ 1 : i² + j² ≤ n²} = Σᵢ₌₁ⁿ ⌊√(n² − i²)⌋.
- Cells that touch the circle at their corner count as inside: a(5) = 15
  needs the corners (3, 4) and (4, 3). The OEIS terms follow this reading.
- `range(n)` runs i = 0 … n−1: the term for i = n is 0, and the i = 0 term
  ⌊√n²⌋ = n is cancelled by the `-1` on each of the n terms, which costs
  the same as writing `range(1,n)`.
- `isqrt` is exact for integers of every size.

**Notes**

- O(n) per term; counting the lattice points with a double loop is the
  same length without the import, but O(n²) per term.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001182), CC BY-SA 4.0.
