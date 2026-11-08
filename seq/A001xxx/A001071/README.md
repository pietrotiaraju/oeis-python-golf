# A001071

> Number of one-sided chessboard polyominoes with n cells.
> — [OEIS A001071](https://oeis.org/A001071)

Offset 1: 2, 1, 4, 10, 36, 108, 392, 1363, 5000, 18223, 67792, 252938, 952540, 3602478, 13699554, 52296713, 200406388, 770411478, 2970401696, 11482395526, …

Polyominoes cut from a chessboard, so every cell is black or white and
neighbours differ. In this sequence two of them are the same when their
shapes are related by a rotation and a translation, and their colourings
are related by any symmetry, reflections included (Joseph Myers, OEIS
comment). The plain one-sided count, where the colours must match under
the rotation itself, is [A121198](https://oeis.org/A121198); the two first
differ at n = 6 (108 here, 110 there).

### Python 3 — 271 bytes

```python
U=1,1j,-1,-1j;F=frozenset;S=[F([0])]
K=lambda Q,f=2,c=0:F(F(u*((w:=len(Q)*z-sum(Q))-m*w.real)+(z*z+c).real%2*f/4for z in Q)for m in(0,f)for u in U)
while[print(sum((K(Q)!=K(Q,2,1))+1for Q in S))]:S={K(Q,0):Q for P in S for Q in{P|{z+d}for z in P for d in U}-{P}}.values()
```

**How it works**

- A shape has two colourings. Under the rule above the coloured pieces of
  one one-sided shape fall into two classes, or into one when some
  symmetry of the shape (rotation, reflection or translation) swaps the
  colours. So a(n) is the sum over the one-sided n-ominoes
  ([A000988](../A000988/)) of 1 + [the two colourings are not related by
  any symmetry]; this is the OEIS formula 2·A000988(n) − … counted
  directly.
- The polyominoes are grown as in [A000988](../A000988/): cells are
  Gaussian integers, `S` keeps one shape per one-sided class, keyed by
  `K(Q,0)`, and each step adds a neighbour `z+d` to every stored shape.
  It starts from the monomino, since the offset is 1.
- `K` centres a shape at its centre of mass, scaled by its size so it
  stays integral: `w:=len(Q)*z-sum(Q)`. It then takes the set of its
  images under the rotations `u` and, for `m=2`, the mirror images
  w − 2·Re w = −w̄ (the trick of [A000105](../A000105/)). With `f=0` the
  mirror loop is `(0,0)` and the colour term vanishes, which gives the
  one-sided key of A000988; with `f=2` it is the key of the coloured shape
  up to all symmetries.
- The colour of a cell rides on its image as an offset of ½ after the
  symmetry is applied: the images are Gaussian integers, so `+½` can never
  be mistaken for another cell. The colour is the parity of x + y, which
  is that of x² − y² = Re z², written `(z*z+c).real%2`; `c=1` swaps the
  colours. `K(Q)!=K(Q,2,1)` says that no symmetry of the shape swaps them.

**Notes**

- Exact arithmetic: complex numbers hold their parts as floats, and every
  part here is an integer (or a half) far below 2⁵³.
- a(n) grows like 4ⁿ and every one-sided shape is built and keyed (twice
  more for the colours): 10 terms print in about 14 s and 11 in about
  57 s here, in about 235 MB. The b-file has the 23 known terms (from
  the OEIS data); the bar is 9 terms in 60 s.
- Without the shared `K` (the one-sided key written out as in A000988 and
  the coloured keys in a loop over `c`) it is 302 bytes but twice as fast.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 271 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001071), CC BY-SA 4.0.
