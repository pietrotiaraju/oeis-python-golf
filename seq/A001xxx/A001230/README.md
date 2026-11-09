# A001230

> Number of undirected closed knight's tours on a 2n X 2n chessboard.
> — [OEIS A001230](https://oeis.org/A001230)

Offset 1: 0, 0, 9862, 13267364410532

a(n) is the number of Hamiltonian cycles of the knight's graph of the
2n × 2n board, a cycle and its reverse counted once.

### Python 3 — 210 bytes

```python
g=lambda p,S:all(len(N[w]&S)>1for w in S-{p,0})and sum(g(q,S-{p})for q in N[p]&S)or{0}==S
n=2
while 1:V={x%n+x//n*1j for x in range(n*n)};N={p:{q for q in V if abs(p-q)==5**.5}for p in V};print(+g(1+2j,V));n+=2
```

**How it works**

- `n` is the side 2, 4, 6, …; a square (x, y) is the complex number
  x + yi, and `N[p]` holds the squares a knight's move from p: |p − q| = √5
  exactly when q − p is (±1, ±2) or (±2, ±1), since 5 is a sum of two
  squares only as 1 + 4.
- From side 4 on, the corner 0 has exactly two neighbours, a = 1+2i and
  b = 2+i. So every closed tour contains the edges a–0 and 0–b, and
  reading it from a, away from 0, gives the walk a → … → b → 0 through
  every square once. Each undirected tour gives exactly one such walk (its
  other direction starts a → 0), and each such walk closes into a tour,
  because 0 is next to a. So a(n) is the number of these walks, with no
  division by 2.
- `g(p,S)` counts the ways to finish a walk whose head is p, where `S`
  holds the unvisited squares, the head and 0 (0 stays in `S` until the
  walk enters it). A step goes to a neighbour q in `S` and drops p. The walk
  is complete when `S` is {0}: the head has just entered 0 after every
  other square. Entering 0 early leads nowhere: from a as the first step,
  0 leaves `S` and can never be the last square; from b later, both
  neighbours of 0 are used and there is no step left.
- Pruning: every unvisited square w other than 0 still needs two tour
  edges, both to squares in `S` (the head, an unvisited square, or 0 for
  b). If fewer than two of its neighbours are in `S`, no walk finishes, so
  `all(len(N[w]&S)>1for w in S-{p,0})` returns False (0) for that branch.
  This only skips branches with no completion, so the count is exact.
- The sum adds the booleans of the leaves. On the 2 × 2 board no square has
  a neighbour, the check fails at once, and `+` turns that False (and the
  False of an empty 4 × 4 search) into 0.

**Notes**

- Correct for every n: the program is an exhaustive search of the
  knight's graph of the 2n × 2n board, and the only facts it uses are that
  the corner has degree two (true for every side ≥ 4) and that a
  Hamiltonian cycle needs two free neighbours at every unvisited square.
  The same function counts 16, 176 and 8 closed tours on the 3 × 10,
  3 × 12 and 5 × 6 boards, the known values.
- a(3) = 9862 comes after about 27 s here (14 reference seconds); a(4) =
  13267364410532 (McKay, 1997) is far out of reach of a search that lists
  the tours one by one.
- A first version counted the directed tours from 0 and halved them, with
  the set for the check as a third argument (225 bytes); it walks both
  directions and took 45 s. A weaker check, only "no square in `S` without
  a neighbour in `S`" (`all(N[w]&S for w in S)`, 198 bytes), had
  not reached a(3) after 300 s.
- The b-file is the OEIS entry's 4 terms; the bar is the first 3 in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 210 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001230), CC BY-SA 4.0.
