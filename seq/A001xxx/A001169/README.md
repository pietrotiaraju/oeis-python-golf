# A001169

> Number of board-pile polyominoes with n cells.
> — [OEIS A001169](https://oeis.org/A001169)

Offset 1: 1, 2, 6, 19, 61, 196, 629, 2017, 6466, 20727, 66441, 212980, …

### Python 3 — 60 bytes

```python
print(1);a,b,c=2,6,19
while 1:print(a);a,b,c=b,c,5*c-7*b+4*a
```

**How it works**

- A board-pile polyomino is one whose every vertical cross-section is a
  single run of cells (one "board"): a column-convex polyomino, the class
  A(1) of Zeilberger's *The umbral transfer-matrix method III* (his A(2) is
  [A001170](../A001170/)). Temperley (1956) found their generating function,
  x(1−x)³/(1 − 5x + 7x² − 4x³).
- The numerator has degree 4, one more than the denominator, so
  a(n) = 5a(n−1) − 7a(n−2) + 4a(n−3) holds from n = 5 on: a(1) = 1 is
  printed apart and the loop starts from a(2), a(3), a(4) = 2, 6, 19.
  No integer a(1) would fit the recurrence (it would have to be 3/4).

**Notes**

- Exact integers; all 200 terms of the b-file at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 60 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001169), CC BY-SA 4.0.
