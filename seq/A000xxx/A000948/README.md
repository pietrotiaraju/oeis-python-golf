# A000948

> Number of free nonplanar polyenoids with n nodes and symmetry point group C_s.
> — [OEIS A000948](https://oeis.org/A000948)

Offset 7: 0, 3, 20, 99, 450, 1896, 7771, 30895, 121144, 468409, 1796584, 6841014, 25925062

The geometrically nonplanar polyenoids of [A000953](../A000953/) (trees
on the honeycomb lattice whose drawing puts two carbons on one lattice
point) that have no symmetry: as in Cyvin et al. (J. Chem. Inf. Comput.
Sci. 35 (1995) 743–751), the symmetry of a nonplanar polyenoid is that of
its drawing, overlap ignored, and C_s means no rotation and no mirror
line in the plane. All polyenoids with no symmetry are the asymmetric
triangulations of an (n + 2)-gon, [A000131](../A000131/), so
a(n) = A000131(n + 2) − A000941(n) (Sean A. Irvine); the planar part has no
formula.

### Python 3 — 284 bytes

```python
S={b'13'*3};n=p=k=0
while[n<6or print(sum((x in(x+x)[1:-1]+b'.'+x[::-1]*2)<1>len({p for c in x if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})-n for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]}
```

**How it works**

- `S` grows one contour word per free polyenoid with n + 1 carbons, planar
  or not, exactly as in [A000953](../A000953/) (the walk and the words are
  explained in [A000942](../A000942/)).
- The symmetry test on the word is that of [A000941](../A000941/): a
  rotation of the shape makes the cyclic word equal to a nontrivial
  rotation of itself (a window of `(x+x)[1:-1]`), and a mirror line makes
  it a rotation of the reversed word (a window of `x[::-1]*2`); the
  separator `b'.'` keeps windows from straddling the two parts. C_s is
  neither, `(x in…)<1`.
- The chain `(…)<1>len(…)-n` also asks for 1 > (number of carbon
  points) − n, that is at most n points for the n + 1 carbons: an overlap.
- `n<6or print(…)` starts the output at 7 carbons, the offset.

**Limits**

- All polyenoids are built, about 3.5ⁿ of them: a(7)…a(13) print in about
  13 s and a(14) in about 55 s; a(15) would take about four times as long
  again. The bar is 6 terms in 120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program for the planar part (honeycomb
  subtrees under the 12 lattice symmetries, n ≤ 11), against A000131 for
  all asymmetric ones, and against Table 7 of Cyvin et al. and the OEIS
  data.
- The b-file is the 13 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 284 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000948), CC BY-SA 4.0.
