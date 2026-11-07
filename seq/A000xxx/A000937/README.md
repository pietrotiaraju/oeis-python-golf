# A000937

> Length of longest simple cycle without chords in the n-dimensional hypercube graph. Also called n-coil or closed n-snake-in-the-box problem.
> — [OEIS A000937](https://oeis.org/A000937)

Offset 1: 0, 4, 6, 8, 14, 26, 48, 96, …

### Python 3 — 144 bytes

```python
P=[1]
g=lambda v,F,B:max([w in P or-~g(w,F|N,B|2*w)for N in[{v^j for j in P}]for w in N-F if w<=B]+[1-B])
for j in P:print(g(1,{0},3)+2);P+=2*j,
```

**How it works**

- Exhaustive search. Every coil can be moved by a symmetry of the cube so
  that it passes through 0 with first edge 0 → 1. `P` is the list of
  one-bit masks 1, 2, 4, … (one more per term, so it has n entries), and a
  vertex w is a neighbour of 0 exactly when `w in P`.
- `g(v,F,B)` extends the chordless path 0, 1, …, v. `F` holds 0 and the
  neighbours of every path vertex before v, so the extensions that keep
  the path chordless are `N-F`, with `N` the neighbours of v. A step onto
  a neighbour of 0 has to close the cycle (anything else adjacent to 0
  would be a chord) and scores 1; any other step recurses with `F|N` and
  adds 1. Lengths count from the root, so the answer is g + 2.
- Symmetry breaking: relabel coordinates so that new directions appear in
  the order 0, 1, 2, …. With U the OR of the path vertices, `B` = 2U+1,
  and a step to w is allowed only if w ≤ B (it uses at most the next new
  bit); `B|2*w` updates it. This cuts the search by about (n−1)!: without
  it n = 6 takes minutes.
- A dead end returns `1-B`, which is below every real score: the path uses
  k directions, so it has at most 2ᵏ vertices, while B = 2ᵏ⁺¹−1. For
  n = 1 (no cycle at all) the answer is 1−3+2 = 0.
- The root passes F = {0}, not {0, 1}. Then at v = 3 the old vertex 1 looks
  like a closing step and scores 1, but the real 4-cycle 0, 1, 3, 2 scores
  1 at the same node, so the maximum does not change. Vertex 1 is adjacent
  to no later path vertex (they all avoid its neighbourhood), so this is
  the only place where it shows up.
- `for j in P:…;P+=2*j,` grows the list it is iterating over, 1 B under
  `while[print(…)]:P+=2*P[-1],`.

**Notes**

- Exact search, no theorem needed.
- a(6) = 26 comes after about 2.5 s; a(7) = 48 (itself only settled by a
  large computer search) did not come within 5 minutes.
- The b-file has 8 terms; the bar is 6 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 144 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000937), CC BY-SA 4.0.
