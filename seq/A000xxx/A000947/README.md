# A000947

> Number of free nonplanar polyenoids with n nodes and symmetry point group C_{2v}.
> — [OEIS A000947](https://oeis.org/A000947)

Offset 7: 1, 2, 4, 10, 15, 44, 56, 177, 212, 706, 792, 2714, 2961

The geometrically nonplanar polyenoids of [A000953](../A000953/) (trees
on the honeycomb lattice whose drawing puts two carbons on one lattice
point) whose only symmetry is one mirror line: as in Cyvin et al. (J.
Chem. Inf. Comput. Sci. 35 (1995) 743–751), the symmetry of a nonplanar
polyenoid is that of its drawing, overlap ignored. Every coiled chain is
of this kind; the coiled C₇H₉ is a(7) = 1. All polyenoids with exactly a
mirror symmetry are the symmetrical triangulations of an (n + 2)-gon,
[A000063](../A000063/), so a(n) = A000063(n + 2) − A000936(n) (Sean A.
Irvine); the planar part has no formula.

### Python 3 — 283 bytes

```python
S={b'13'*3};n=p=k=0
while[n<6or print(sum((x in(x+x)[1:-1])<(x[::-1]in x+x)>len({p for c in x if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})-n for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]}
```

**How it works**

- `S` grows one contour word per free polyenoid with n + 1 carbons, planar
  or not, exactly as in [A000953](../A000953/) (the walk and the words are
  explained in [A000942](../A000942/)).
- The symmetry tests on the word are those of [A000936](../A000936/): a
  rotation of the shape is `x in(x+x)[1:-1]` (the cyclic word equals a
  nontrivial rotation of itself) and a mirror line is `x[::-1]in x+x` (the
  reversed word is a rotation of the word). C₂ᵥ is a mirror and no
  rotation.
- The chain `R<M>len(…)-n` reads: no rotation, a mirror, and
  1 > (number of carbon points) − n, that is at most n points for the
  n + 1 carbons: an overlap.
- `n<6or print(…)` starts the output at 7 carbons, the offset.

**Limits**

- All polyenoids are built, about 3.5ⁿ of them: a(7)…a(13) print in about
  10 s and a(14) in about 45 s; a(15) would take about four times as long
  again. The bar is 6 terms in 120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program for the planar part (honeycomb
  subtrees under the 12 lattice symmetries, n ≤ 11), against A000063 for
  all mirror-symmetric ones, and against Table 7 of Cyvin et al. and the
  OEIS data.
- The b-file is the 13 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 283 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000947), CC BY-SA 4.0.
