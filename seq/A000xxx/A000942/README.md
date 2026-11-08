# A000942

> Number of free planar polyenoids with n nodes.
> — [OEIS A000942](https://oeis.org/A000942)

Offset 1: 1, 1, 1, 3, 4, 12, 26, 77, 204, 624, 1817, 5585, 17007, 52803, 164001, 514009, …

A polyenoid (Cyvin, Brunvoll, Brendsdal, Cyvin and Lloyd, J. Chem. Inf.
Comput. Sci. 35 (1995) 743–751) is a tree drawn on the honeycomb lattice:
its nodes are carbon atoms on lattice points and its edges are lattice
bonds, so any two bonds at a carbon meet at 120°. It stands for a
conjugated polyene CₙHₙ₊₂, the hydrogens sitting on the free lattice
directions. It is *geometrically planar* when no two carbons fall on the
same lattice point (bonds cannot cross otherwise), and *free* means
counted up to rotations and reflections. Up to n = 6 every polyenoid is
planar; the first overlap is the coiled C₇H₉, whose seventh carbon lands
on the first. No formula is known, so the program lists the shapes. The
same program, with a different count at the end, does the symmetry
classes [A000935](../A000935/), [A000936](../A000936/),
[A000941](../A000941/) and the nonplanar ones [A000947](../A000947/),
[A000948](../A000948/), [A000953](../A000953/).

### Python 3 — 236 bytes

```python
S={b'13'*3};n=p=k=0
while[print(len(S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]if len({p for c in v if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})>n}
```

**How it works**

- Contour words. Walk once around the tree, hugging it, with the hydrogens
  as leaves: every carbon is passed three times and every hydrogen once,
  so n carbons give a cyclic word of length 4n + 2 over `1` (a carbon) and
  `3` (a hydrogen). Methyl is `131313`. The word fixes the shape; starting
  the walk elsewhere rotates the word, and the mirror image reverses it.
  So the key of a free polyenoid is the least rotation of its word or of
  the reversed word, `min(r[j:]+r[:j]for r in(v,v[::-1])…)`, and `S` holds
  these keys.
- Growth: putting a CH₂ in place of a hydrogen turns that `3` into `13131`
  (reach the new carbon, a hydrogen, back, a hydrogen, back, leave). Every
  polyenoid with n + 1 carbons comes from one with n carbons this way (cut
  off an end carbon), and the cut keeps a planar shape planar, so it is
  enough to grow the planar ones.
- Drawing: on the walk the heading turns by 60° at a carbon and by 180°
  at a hydrogen, so in units of 60° the turn is the digit itself. In a
  bytes object the digits are 49 and 51, which are 1 and 3 mod 6, so
  `k:=k+c` keeps the heading k (mod 6) with no `int`, and `c&2` (0 or 2)
  picks out the hydrogens.
- The steps are drawn on the brick wall, the usual picture of the honeycomb
  as a square grid in which every lattice point has a left and a right
  neighbour and one more above or below. The six headings 330°, 30°, 90°,
  150°, 210°, 270° become the Gaussian-integer steps 1, 1, i, −1, −1, −i,
  which is `1j**(k%6//1.5)` (k mod 6 = 0, 1, …, 5 gives the exponents 0, 0,
  1, 2, 2, 3). The brick wall is the honeycomb graph itself, so two
  carbons land on the same point exactly when they coincide in the
  honeycomb.
- `len({…})>n` asks for n + 1 different points among the carbon visits
  (each carbon is passed three times on the same point). The walk steps,
  then turns at the node `c` names, so `p` is the point of that node. The
  list `[p:=…,k:=…]` is built for every letter, and `c%3*` (49 % 3 = 1,
  51 % 3 = 0) leaves it non-empty only at a carbon, which is then
  recorded.
- `p` and `k` are never reset: a whole contour turns through a multiple of
  360° and ends where it started, so every walk starts at the same point
  with the same heading mod 6.
- `range(9*n)` covers every rotation of the 4n + 6 letters of a child once
  n ≥ 2 (a larger j just gives the word back). For n = 1 the only child is
  ethylene, whose word has period 5, so 9 shifts are enough there too.

**Limits**

- a(n) grows like 3.2ⁿ and the program builds every shape: a(1)…a(13)
  print in about 16 s and a(14) in about 60 s; a(15) = 164 001 would take
  about four times as long again. The bar is 11 terms in 120 s.
- The arithmetic is exact: positions are Gaussian integers with parts below
  4n, held exactly by the floats of a complex number, and CPython computes
  a power of a complex number to a whole exponent of size at most 100
  (here 0 to 3; `//1.5` gives a float, but a whole one) by repeated
  multiplication.

**Notes**

- Checked against an independent program, which grows honeycomb subtrees
  as sets of vertices and edges and compares them under the 12 lattice
  symmetries: the same counts, symmetry class by symmetry class, for
  n ≤ 11, and the same as Table 6 of Cyvin et al. (n ≤ 15) and the OEIS
  data.
- Tuples (`(1,3)*3` and `(1,3,1,3,1)`; `c&2` and `c%3` work there too)
  are 2 bytes longer, run at about half the speed and lose the substring tests
  that the class programs use. Strings would need `int(c)` and a
  separate carbon test.
  `range(4*n+6)` (exactly the rotations) is 2 bytes longer and about twice
  as fast.
- The b-file is the 20 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 236 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000942), CC BY-SA 4.0.
