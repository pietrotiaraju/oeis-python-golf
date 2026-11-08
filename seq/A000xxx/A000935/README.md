# A000935

> Number of free planar polyenoids with 2n nodes and symmetry point group C_{2h}.
> — [OEIS A000935](https://oeis.org/A000935)

Offset 1: 0, 1, 2, 7, 20, 63, 191, 598, 1870, 5906

The planar polyenoids of [A000942](../A000942/) (trees on the honeycomb
lattice, standing for polyenes CₙHₙ₊₂) whose only symmetry in the plane
is the half turn about their centre, which with the molecular plane makes
the point group C₂ₕ; trans-butadiene is the first (a(2) = 1). The centre
of such a tree is the midpoint of a bond, so the number of carbons is
even, and a(n) counts those with 2n carbons. No formula is known.

### Python 3 — 284 bytes

```python
S={b'13'*3};n=p=k=0
while[n%2and print(sum((x[2*n+3:]*2==x)>(x[::-1]in x+x)for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]if len({p for c in v if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})>n}
```

**How it works**

- Apart from the count inside `print`, this is the program of
  [A000942](../A000942/): `S` holds one contour word per free planar
  polyenoid with n + 1 carbons (a cyclic word over `1` for a carbon and `3`
  for a hydrogen, read once around the tree), and each round puts a CH₂
  in place of a hydrogen and keeps the children whose drawing on the
  honeycomb has no repeated carbon. That page explains the walk.
- `n%2and print(…)` prints only when the number of carbons n + 1 is even.
- A half turn of the shape shifts its contour by half: the word of length
  4(n + 1) + 2 is its second half twice, `x[2*n+3:]*2==x`. (A third of a
  turn would be a different shift, and the C₃ₕ shapes with 10, 16, …
  carbons do not pass this test.) A mirror line reverses the contour, so
  the reversed word is a rotation of the word, `x[::-1]in x+x`; a half
  turn with a mirror is D₂ₕ. So C₂ₕ is "half turn and no mirror",
  `True>False`.

**Limits**

- The program builds every planar shape (they grow like 3.2ⁿ per carbon):
  a(1)…a(6) print in about 4 s and a(7), with 14 carbons, in about 50 s;
  a(8) needs two more sizes, more than ten times as long. The bar is 6
  terms in 120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program (honeycomb subtrees under the 12
  lattice symmetries, with the stabilizer read off directly) for up to 10
  carbons, and against Table 6 of Cyvin et al. and the OEIS data.
- The b-file is the 10 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 284 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000935), CC BY-SA 4.0.
