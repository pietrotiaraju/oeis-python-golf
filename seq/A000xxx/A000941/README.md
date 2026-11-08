# A000941

> Number of free planar polyenoids with n nodes and symmetry point group C_s.
> — [OEIS A000941](https://oeis.org/A000941)

Offset 1: 0, 0, 0, 0, 2, 5, 21, 58, 194, 570, 1790, 5434, 16924, 52362, 163784, 512670, …

The planar polyenoids of [A000942](../A000942/) (trees on the honeycomb
lattice, standing for polyenes CₙHₙ₊₂) that have no symmetry in the plane:
their point group is just C_s, the reflection in the molecular plane. A
planar polyenoid belongs to D₃h, C₃h, D₂h, C₂h, C₂v or C_s (Cyvin et al.,
J. Chem. Inf. Comput. Sci. 35 (1995) 743–751); this is by far the largest
class. No formula is known.

### Python 3 — 279 bytes

```python
S={b'13'*3};n=p=k=0
while[print(sum(x not in(x+x)[1:-1]+b'.'+x[::-1]*2for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]if len({p for c in v if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})>n}
```

**How it works**

- Apart from the count inside `print`, this is the program of
  [A000942](../A000942/): `S` holds one contour word per free planar
  polyenoid with n carbons (a cyclic word over `1` for a carbon and `3` for
  a hydrogen, read once around the tree), and each round puts a CH₂ in
  place of a hydrogen and keeps the children whose drawing on the
  honeycomb has no repeated carbon. That page explains the walk.
- The symmetries of the shape in the plane show up in the word. A rotation
  of the plane that maps the shape to itself shifts the contour, so the
  cyclic word equals one of its own nontrivial rotations:
  `x in(x+x)[1:-1]` (the rotations of x are the length-|x| windows of x+x;
  dropping the two ends leaves only the nontrivial ones). A mirror line
  reverses the contour, so the reversed word is a rotation of the word:
  `x[::-1]in x+x`, or equally x is a window of `x[::-1]*2`. The substring
  tests are why the words are bytes and not tuples.
- C_s is neither, and the two tests fit in one: x has a rotation or a
  mirror exactly when it occurs in `(x+x)[1:-1]+b'.'+x[::-1]*2`. The
  separator byte keeps a window from straddling the two parts, since x
  has no `.` in it.

**Limits**

- a(n) is almost all of A000942 (it grows like 3.2ⁿ), and the program
  builds every planar shape: a(1)…a(13) print in about 15 s and a(14) in
  about 50 s; a(15) would take about four times as long again. The bar is
  11 terms in 120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program (honeycomb subtrees under the 12
  lattice symmetries, with the stabilizer read off directly) for n ≤ 11,
  and against Table 6 of Cyvin et al. and the OEIS data.
- The two tests apart, `(x[::-1]in x+x)|(x in(x+x)[1:-1])<1`, are 1 byte
  longer. The separator is needed: the last byte of `x[::-1]` is `x[0]`,
  so `x[::-1]*2+(x+x)[1:-1]` always contains x across the join.
- The b-file is the 19 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 279 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000941), CC BY-SA 4.0.
