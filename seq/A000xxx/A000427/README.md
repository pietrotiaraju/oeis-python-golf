# A000427

> Number of 7-dimensional partitions of n.
> — [OEIS A000427](https://oeis.org/A000427)

Offset 1: 1, 8, 36, 148, 554, 2024, 7134, 24796, 84625, 285784, …

### Python 3 — 266 bytes

```python
d=8
S={frozenset()}
while S:
 T=set()
 for s in S:
  for v in {(0,)*d}|{tuple(x+(j==i)for j,x in enumerate(u))for u in s for i in range(d)}:
   if v not in s and all(tuple(x-(j==i)for j,x in enumerate(v))in s for i in range(d)if v[i]):T.add(s|{v})
 S=T;print(len(S))
```

**How it works**

- A 7-dimensional partition is a weakly decreasing
  7-dimensional array of nonnegative integers. Replace
  each entry by a stack of that many cells: the result is a finite
  **order ideal in ℕ^8**, a set containing every cell below
  each of its cells in the coordinatewise order.
- S contains all ideals of the current size. It starts with the
  single empty ideal, `S={frozenset()}`. An ideal s is itself
  immutable so it can be stored as an element of the outer set.
- A new cell is either the origin `(0,)*d` or one step above
  an existing cell along one of the d=8 axes. The nested
  comprehension increments coordinate i using `x+(j==i)`;
  the candidate set merges cells generated from several neighbors.
- Accept v only if it is new and every immediate lower neighbor
  is present. The generator checks axis i only when `v[i]` is
  positive, avoiding negative coordinates. Since s is already an
  ideal, having these immediate neighbors also supplies every
  more distant lower cell.
- `T.add(s|{v})` stores an ideal with one extra cell. Different
  choices of the removed maximal cell can lead to the same ideal;
  T deduplicates those constructions by exact equality of the cell
  sets. Coordinate permutations remain distinct.
- After all extensions, `S=T;print(len(S))` advances the size
  and prints its count. The origin is the only one-cell ideal,
  giving a(1)=1; extending it in any of 8 axes gives
  a(2)=8.

**Notes**

- Completeness follows by removing a maximal cell from any nonempty
  ideal. The remainder is a smaller ideal, and the removed cell
  is one of its allowed extensions. Induction therefore reaches
  every ideal of every size, with exact integer counts.
- The axes are fixed. Identifying configurations under rotations
  would instead count a different sequence; frozenset equality
  here only removes duplicate paths to the same configuration.
- Every ideal in a layer is stored, and each can produce several
  copied cell sets. The rapidly growing layer sizes dominate both
  time and memory. A chain exists at every size, so S never empties
  mathematically; resource limits stop practical runs.
- [A000416](../A000416/) changes only d by one.
  [A000428](../A000428/) is the corresponding
  MacMahon Euler-product prediction, which already differs at
  n=6; it cannot replace this exhaustive count.
- The b-file has 20 terms (indices 1 through 20). The bar is the
  first 7 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 266 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000427), CC BY-SA 4.0.
