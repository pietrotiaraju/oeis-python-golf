# A001111

> Number of inequivalent Hadamard designs of order 4n.
> — [OEIS A001111](https://oeis.org/A001111)

Offset 1: 1, 1, 1, 5, 6, 1106, 208310, 10374196953

a(n) is the number of symmetric 2-(4n − 1, 2n − 1, n − 1) designs up to
isomorphism (an OEIS comment): n = 1 is three singletons, n = 2 the Fano
plane, n = 3 the 2-(11,5,2) biplane, then five 2-(15,7,3) designs and six
2-(19,9,4) designs. There is no formula; the known terms are computer
classifications (Spence up to n = 7, McKay for n = 8). The program
enumerates the designs and keeps one canonical incidence matrix per class,
so it is exact for every n but only reaches n = 5.

### Python 3 — 423 bytes

```python
B=int.bit_count
C=lambda U,T,P:next((q for b in U if[r:=0]+[r:=r<<B(c)|2**B(b&c)-1for c in P]and(q:=2*(r<T[0])or r==T[0]and C([u for u in U if u-b],T[1:],[x for c in P for x in(c&~b,c&b)if x]))>(U==T)),[]==T)
G=lambda R,S,D,d=0:(d%v>6or C(R,R,[2**v-1])<2)and sum((G(R+[x],[y for y in S if B(x&y)-v//4==0<y-x],D|x*2^x,d+1)for x in S if x&~(x*2|D)<1),d==v)
v=3
while[print(G([],[x for x in range(2**v)if B(x)==v//2],1))]:v+=4
```

**How it works**

- **What is searched.** With v = 4n − 1, k = 2n − 1 = `v//2` and
  λ = n − 1 = `v//4`, a block is a v-bit integer (bit p = point p). Since
  k(k − 1) = λ(v − 1), v distinct k-sets that pairwise meet in exactly λ
  points already form a symmetric 2-(v, k, λ) design: if the incidence matrix
  N has row sums k and NNᵀ = (k − λ)I + λJ, it is invertible, its column sums
  are k as well and NᵀN = (k − λ)I + λJ, which says every pair of points lies
  in λ blocks (Ryser). So `G` only adds k-sets meeting every chosen block in
  λ points: the list `S` passed down keeps exactly those.
- **Canonical form.** Isomorphism permutes the points (columns) and the
  blocks (rows). Each class has one lexicographically smallest incidence
  matrix (rows as integers, compared in order), and a(n) is the number of
  matrices that are their own minimum. The smallest matrix has increasing
  rows (`y>x`, with `S` sorted) and sorted columns: for neighbouring bits
  p + 1 and p, the column of p + 1 read top-down is the smaller one. `D` has
  bit p + 1 set once the two columns differ (`D|x*2^x`); while they are still
  equal, a new row may not have 1 at p + 1 and 0 at p (`x&~(x*2|D)<1`). With
  all columns equal at the start, only 2ᵏ − 1 passes as the first row, so the
  first block needs no special case; `D` starts at 1 because bit 0 has no
  lower neighbour.
- **Canonicity test `C(U,T,P)`.** A branch and bound over the orders in
  which the blocks can be listed: `T` holds the target rows still to match,
  `U` the blocks still unused and `P` the cells, the ordered classes of
  columns that agree on the blocks chosen so far. The smallest row a block
  `b` can produce next puts, inside each cell, its 0s first and its 1s at the
  low end: `r=r<<B(c)|2**B(b&c)-1`. If r is below the target row the matrix
  is not minimal (2 is returned all the way up); if equal, the cells are
  split into `c&~b`, `c&b` and the search goes one row deeper; if larger, `b`
  is skipped. A matrix of this shape that is not minimal always loses at some
  row, so this decides minimality exactly.
- **Automorphism pruning.** Every full path that matches all rows is an
  automorphism. The identity path is searched first (the target's own next
  row is always the first unused block on it). When a path that has left it
  matches to the end, the automorphism maps the identity subtree at the same
  depth (already searched completely) onto the subtree where the path left;
  so that whole subtree is abandoned and 1 travels up to the nearest node of
  the identity path, which goes on with its next block. Nodes of the identity
  path are recognised by `U==T` (the unused blocks are exactly the remaining
  target rows, in order). Some nodes off the path pass that test too; they
  then keep searching after a 1 instead of passing it up, which prunes less
  but never wrongly. Without
  this, the 20 160 automorphisms of PG(3,2) make one test take seconds.
- **Pruning partial matrices.** The first d rows of a minimal matrix are the
  minimal matrix of those d blocks (otherwise reordering them would give a
  smaller full matrix), so `C` also runs on partial matrices up to depth 6
  (`d%v>6or`). At depth v it is always run, and `sum(…,d==v)` counts the
  complete matrices that pass.
- **Why the count is exact.** The minimal matrix of each class satisfies all
  the generator's constraints and passes every test, so it is counted; any
  other complete matrix fails `C` at depth v. No invariants are used. `C`
  was also checked against brute force (the minimum over all column
  permutations) on about 2600 matrices of this shape, from random and highly
  symmetric families on up to 7 points, among them all k-subsets of a set.

**Notes**

- Times on this PC: n = 4 in 0.8 s, n = 5 in 25 s (peak about 75 MB).
  n = 6, with 1106 classes of 2-(23,11,5) designs, is far out of reach. The
  bar is 5 terms in 120 s.
- The depth limit 6 is a speed setting, not a correctness one: with limits
  5 or 7, or with the test at every depth, n = 5 did not finish within
  100 s.
- Other shapes tried: the lexicographically largest matrix as canonical
  form (rows decreasing, a few bytes longer); dropping the cells for per-point column
  codes compared as sorted lists (longer). Skipping a node when fewer than
  v − d candidates are left (`len(S)+d>=v and`, +16 bytes) makes n = 5 run in
  7 s.
- The OEIS has no separate b-file; the one here is the 8 terms of the entry.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 423 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001111), CC BY-SA 4.0.
