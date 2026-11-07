# A000791

> Ramsey numbers R(3,n).
> — [OEIS A000791](https://oeis.org/A000791)

Offset 1: 1, 3, 6, 9, 14, 18, 23, 28, 36, …

### Python 3 — 125 bytes

```python
f=lambda F,m=1:max(map(len,F))<k and max(m,*[f(F|{T-N|{m}for T in F},m+1)for N in F])
k=1
while[print(f({frozenset()}))]:k+=1
```

**What is computed**

R(3,n) is the least m such that every graph on m vertices has a triangle or
an independent set of n vertices. So R(3,n) − 1 is the largest order of a
triangle-free graph with independence number α < n, and the program finds
that order by exhaustive search (k = n in the code).

**How it works**

- **A graph is stored as its independent sets.** F is the set of all
  independent sets (frozensets) of the current graph on the vertices
  1, …, m−1; the empty graph is `{frozenset()}`. The family determines the
  graph, and it is all the search needs.
- **Adding vertex m.** Its neighbourhood N is any member of F: N must be
  independent, or m would close a triangle, and every independent N is
  allowed. The independent sets of the new graph are the old ones plus
  T ∪ {m} for every old T disjoint from N; `T-N|{m}` over all T in F lists
  exactly these (T − N is itself independent and disjoint from N), and the
  set union drops the repeats.
- **The bound α < n.** A child whose family has a set of k or more vertices
  fails `max(map(len,F))<k` and returns False, which counts as 0 in the max.
  Otherwise f returns the largest m reached below it, at least its own m,
  which is the current order plus one; at the root that is R(3,n).
- `max(m,*[…])` never sees an empty list (N = ∅ is always a child) and is a
  byte under `max([m]+[…])`.

**Correctness**

Every triangle-free graph with α < n is reached: its first j vertices induce
such a graph for every j, and each vertex's neighbourhood among the earlier
ones is one of the N tried. The search is finite because the properties are
hereditary and R(3,n) ≤ C(n+1,2) (Erdős–Szekeres), so no assumption about
the answer is used; open values such as R(3,10) would come out of the same
search, only far too slowly.

**Speed**

The search runs over labeled graphs, with no isomorphism rejection: R(3,4) = 9
needs about 35 000 graphs and takes about 37 s here, while R(3,5) = 14 would
have to visit every labeling of the unique (3,5)-graph on 13 vertices, more
than 10⁸ of them. The bar is the first 4 terms within 120 s. Memory stays
tiny (depth-first).

**Notes**

- The same search with bitmasks in a list, testing each N before building
  the child (`for N in F if all(T&N or T.bit_count()<k for T in F)`), takes
  about 4 s for the 4 terms but is 142 bytes.
- Bitmasks in a set (`{0}`, `T&~N|1<<m`, `map(int.bit_count,F)`) are 129
  bytes: `{frozenset()}` costs 10 bytes more than `{0}`, but `len` and
  `T-N|{m}` win them back.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 125 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000791), CC BY-SA 4.0.
