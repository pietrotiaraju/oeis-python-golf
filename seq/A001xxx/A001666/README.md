# A001666

> Number of n-step self-avoiding walks on b.c.c. lattice (version 2).
> — [OEIS A001666](https://oeis.org/A001666)

Offset 0: 1, 8, 56, 392, 2648, 17960, 120056, 804824, 5351720, 35652680, …

The body-centred cubic lattice: the points (x, y, z) with x, y, z all even
or all odd, each joined to its eight neighbours (x ± 1, y ± 1, z ± 1). A
walk starts at the origin, makes n steps and never visits a point twice;
a(n) counts these walks (all directions, no symmetry reduction). That is
the convention of the data: a(1) = 8, a(2) = 8·7, a(3) = 8·7² (the lattice
has no triangles), and a(4) = 2648 = 8·7³ − 96 drops the 96 closed
4-step walks of [A001667](../A001667/).

### Python 3 — 116 bytes

```python
f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for d in(1,B,B*B,B*B-~B)for w in{p+d,p-d}-S)
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- Lattice coordinates: e₁ = (1, 1, −1), e₂ = (1, −1, 1), e₃ = (−1, 1, 1)
  are neighbour steps and a basis of the lattice, and the fourth neighbour
  pair is ±(e₁ + e₂ + e₃) = ±(1, 1, 1). So in coordinates c the eight steps
  are ±(1,0,0), ±(0,1,0), ±(0,0,1), ±(1,1,1).
- Code: c ↦ c₁ + c₂B + c₃B², so the steps are `p±d` for d = 1, B, B², and
  B² + B + 1, written `B*B-~B`.
- B = n + 1 (it starts at 1 and grows by one per term). Every step changes
  each coordinate by at most 1, so two points of an n-step walk differ by
  at most n < B in each coordinate. Equal codes then mean
  Δc₁ + Δc₂B + Δc₃B² = 0: B divides Δc₁, so Δc₁ = 0, then likewise Δc₂ = 0
  and Δc₃ = 0. So the code is one-to-one on every walk and `S`, a set of
  integers, is an exact visited set.
- `f(p,S)` counts the ways to finish a walk standing at p with visited set
  S; the walk is complete when it has n + 1 points, `B<=len(S)`, and then
  scores `True`. `+` prints a(0)'s `True` as 1. Same search as the cubic
  lattice [A001412](../A001412/), with four step pairs.

**Golf notes**

- Any basis of three neighbour steps works; the fourth pair is then ± the
  sum of the three with some signs. The codes 1, B, B² and B² + B + 1
  (`B*B-~B`) are as short as any choice found; `1,B,~B*B,B*B+1` ties.
- Cartesian codes x + yB + zB² would need the eight sums ±1 ± B ± B²
  written out.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator); the default recursion limit would
  matter only near n = 490.
- The time grows like the number of walks (about 6.53ⁿ): a(8) comes after
  about 16 s here and a(9) would need about 2 minutes.
- The b-file has 29 terms (a(0) to a(28), from Schram, Barkema, Bisseling
  and Clisby); the bar is 9 terms (up to a(8)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 116 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001666), CC BY-SA 4.0.
