# A001933

> Number of chessboard polyominoes with n squares.
> — [OEIS A001933](https://oeis.org/A001933)

Offset 1: 2, 1, 4, 7, 24, 62, 216, 710, 2570, 9215, 34146, 126853, 477182, 1802673, …

Polyominoes cut from a chessboard, so every cell is black or white and
neighbours differ. Two of them are the same when a symmetry of the board
(translation, rotation or reflection) maps one onto the other with the
colours matching (John Mason, OEIS comment): the black and the white
monomino are two, the domino is one. [A001071](../A001071/) is the
one-sided count.

### Python 3 — 218 bytes

```python
U=1,1j,-1,-1j;F=frozenset;S=F(),
while 1:S={F(F(u*((w:=len(Q)*z-sum(Q))-m*w.real)+(z*z).real%2/2for z in Q)for m in(0,2)for u in U):Q for P in S for Q in{P|{z+d}for z in P or{0,1}for d in U}-{P}}.values();print(len(S))
```

**How it works**

- Cells are Gaussian integers and the colour of a cell z = x + iy is the
  parity of x + y, which is that of x² − y² = Re z², written
  `(z*z).real%2`. `U` holds the four unit steps, which double as the four
  rotations.
- `S` keeps one shape per class of coloured n-ominoes, keyed by the key
  below, so `len(S)` is a(n). Each step adds a neighbour `z+d` to every
  stored shape; `-{P}` drops the cases where `z+d` was already a cell.
  Every coloured polyomino with n + 1 cells is one with n cells plus a
  neighbour (take away a leaf of a spanning tree), and the symmetry that
  maps that smaller one onto its stored representative keeps colours and
  maps neighbours to neighbours, so every class is reached.
- The key, as in [A000105](../A000105/): each cell relative to the centre
  of mass, w = |Q|·z − Σz (scaled by |Q| so it stays a Gaussian integer),
  under the 8 maps `u*` of w or of its mirror image w − 2·Re w = −w̄
  (`m` = 0 or 2), and here each image cell carries + ½ when the cell it
  came from is odd. The images are Gaussian integers, so the tag can never
  be mistaken for another cell.
- Why the key is exact: every symmetry of the board is z ↦ g(z) + t, with
  g one of the 8 rotations and reflections about the cell 0 and t a
  translation. Each g keeps x + y mod 2, so the symmetry keeps the colours
  exactly when t is even (x + y of t even). Two coloured shapes get the
  same key exactly when the centred images match cell for cell with the
  same tags, that is when one is g(Q) + t with every cell keeping its
  colour, that is with t even: the equivalence of the definition.
- The search starts from the empty shape: `P or{0,1}` puts a first cell
  next to 0 or next to 1, which gives both colours, and the first value
  printed is a(1) = 2.

**Notes**

- For odd n the colour counts differ, so no symmetry of a shape can swap
  them and a(n) = 2·A000105(n) (an OEIS formula): 216 = 2·108,
  2570 = 2·1285. The program does not use this.
- a(n) grows about 3.9 times per term and the program keeps every class
  of the last level: 10 terms in about 7 s here, while a(11) needs more
  than 400 MB (memory passes 400 MB after about 29 s). The bar is 10
  terms in 60 s. The b-file has 50 terms.
- Exact arithmetic: complex numbers hold their parts as floats, and every
  part here is an integer or a half of size at most 2n², exact as a float
  for every n below 6·10⁷, far beyond any n a search over 4ⁿ shapes can
  reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 218 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001933), CC BY-SA 4.0.
