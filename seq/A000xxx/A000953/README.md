# A000953

> Number of free nonplanar polyenoids with n nodes.
> — [OEIS A000953](https://oeis.org/A000953)

Offset 7: 1, 5, 24, 109, 465, 1943, 7827, 31095, 121356, 469235, 1797376, 6844290, 25928036

A polyenoid (Cyvin, Brunvoll, Brendsdal, Cyvin and Lloyd, J. Chem. Inf.
Comput. Sci. 35 (1995) 743–751) is a tree drawn on the honeycomb lattice,
standing for a polyene CₙHₙ₊₂; see [A000942](../A000942/). It is
*geometrically nonplanar* (helicenic) when its drawing puts two carbons
on the same lattice point, so that the real molecule has to coil out of
the plane. The smallest is the coiled C₇H₉, whose seventh carbon lands on
the first. All polyenoids, planar or not, are the triangulations of an
(n + 2)-gon up to rotation and reflection, counted by
[A000207](../A000207/), so a(n) = A000207(n) − A000942(n) (Sean A.
Irvine); the planar part has no formula.

### Python 3 — 250 bytes

```python
S={b'13'*3};n=p=k=0
while[n<6or print(sum(len({p for c in x if c%3*[p:=p+1j**(k%6//1.5),k:=k+c]})<=n for x in S))]:n+=1;S={min(r[j:]+r[:j]for r in(v,v[::-1])for j in range(9*n))for w in S for i,c in enumerate(w)if c&2for v in[w[:i]+b'13131'+w[i+1:]]}
```

**How it works**

- This is the program of [A000942](../A000942/) with the planarity filter
  moved from the growth to the count. `S` holds one contour word per free
  polyenoid with n + 1 carbons, planar or not: the cyclic word read once
  around the tree, `1` at each carbon visit and `3` at each hydrogen. Each
  round puts a CH₂ in place of a hydrogen (`3` becomes `13131`) and keeps
  the least rotation of the word or its reverse as the key. Nothing is
  thrown away, so `len(S)` would be A000207.
- The count walks each word on the brick-wall picture of the honeycomb
  (turn 60° at a carbon, 180° at a hydrogen; the A000942 page explains
  `1j**(k%6//1.5)`) and counts the words whose n + 1 carbons land on at
  most n points.
- The words are bytes: iterating gives 49 for `1` and 51 for `3`, which
  are the turns 1 and 3 mod 6, so `k:=k+c` keeps the heading, and
  `c%3*[…]` is non-empty only at a carbon.
- `n<6or print(…)` starts the output at 7 carbons, the offset.

**Limits**

- All polyenoids are built, about 3.5ⁿ of them: a(7)…a(13) print in about
  15 s and a(14) in about 55 s; a(15), from 285 357 shapes, would take
  about four times as long again. The bar is 6 terms in 120 s.
- The arithmetic is exact (Gaussian integers; see A000942).

**Notes**

- Checked against an independent program for the planar part (honeycomb
  subtrees under the 12 lattice symmetries, n ≤ 11), against A000207 for
  the total, and against Table 7 of Cyvin et al. and the OEIS data.
- Tuples (`(1,3)*3` and `(1,3,1,3,1)`) are 2 bytes longer and run at
  about half the speed.
- The b-file is the 13 OEIS terms, so the check stops at the timeout.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 250 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000953), CC BY-SA 4.0.
