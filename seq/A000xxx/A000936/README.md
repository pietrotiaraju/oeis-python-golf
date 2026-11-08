# A000936

> Number of free planar polyenoids with n nodes and symmetry point group C_{2v}.
> — [OEIS A000936](https://oeis.org/A000936)

Offset 1: 0, 0, 1, 1, 2, 4, 4, 12, 10, 29, 27, 88, 76, 247, 217, 722, 638, 2134, 1901, 6413

The planar polyenoids of [A000942](../A000942/) (trees on the honeycomb
lattice, standing for polyenes CₙHₙ₊₂) whose only symmetry in the plane
is one mirror line, which with the molecular plane makes the point group
C₂ᵥ. Examples: the bent C₃ chain of the allyl radical C₃H₅ (a(3) = 1) and
cis-butadiene (a(4) = 1). No formula is known.

### Python 3 — 278 bytes

```python
S={b'13'*3};n=p=k=0
while[print(sum((x[::-1]in x+x)>(x in(x+x)[1:-1])for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]if len({p for c in v if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})>n}
```

**How it works**

- Apart from the count inside `print`, this is the program of
  [A000942](../A000942/): `S` holds one contour word per free planar
  polyenoid with n carbons (a cyclic word over `1` for a carbon and `3` for
  a hydrogen, read once around the tree), and each round puts a CH₂ in
  place of a hydrogen and keeps the children whose drawing on the
  honeycomb has no repeated carbon. That page explains the walk.
- A mirror line of the shape reverses the contour, so the reversed word is
  a rotation of the word: `x[::-1]in x+x`. A rotation of the plane that
  maps the shape to itself shifts the contour, so the word equals one of
  its nontrivial rotations: `x in(x+x)[1:-1]`. A mirror together with a
  rotation would make the group D₂ₕ or D₃ₕ, so C₂ᵥ is "mirror and no
  rotation", the comparison `True>False` of the two booleans.

**Limits**

- a(n) is small, but the program still builds every planar shape (they
  grow like 3.2ⁿ): a(1)…a(13) print in about 15 s and a(14) in about 50 s;
  a(15) would take about four times as long again. The bar is 11 terms in
  120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program (honeycomb subtrees under the 12
  lattice symmetries, with the stabilizer read off directly) for n ≤ 11,
  and against Table 6 of Cyvin et al. and the OEIS data. The table splits
  C₂ᵥ into C₂ᵥ(a) (the axis through a carbon) and C₂ᵥ(b) (the axis across a
  bond); this sequence is the sum.
- The b-file is the 20 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 278 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000936), CC BY-SA 4.0.
