# A001668

> Number of self-avoiding n-step walks on honeycomb lattice.
> — [OEIS A001668](https://oeis.org/A001668)

Offset 0: 1, 3, 6, 12, 24, 48, 90, 174, 336, 648, …

The honeycomb lattice: every point has three neighbours, and the points form
two triangular sublattices; every edge joins the two. A walk starts at a
point, makes n steps along edges and never visits a point twice; a(n) counts
these walks (all directions, no symmetry reduction).

### Python 3 — 96 bytes

```python
f=lambda p,S:B<len(S)*2or sum(f(w,S|{w})for w in{~p,1-p,B-p}-S)
B=1
while[print(+f(0,{0}))]:B+=2
```

**How it works**

- Lattice coordinates: the three edges at an even site point along v₀, v₁,
  v₂ (120° apart), and u₁ = v₀ − v₁, u₂ = v₀ − v₂ span the even sites.
  Write an even site as a₁u₁ + a₂u₂ and an odd site as c₁u₁ + c₂u₂ + v₀;
  then even site a and odd site c are neighbours exactly when c = a,
  c = a − e₁ or c = a − e₂.
- Code, with an odd base B: g(a) = 2a₁ + (B+1)a₂; an even site a gets g(a),
  an odd site c gets ~g(c) = −1 − g(c). The three neighbours of the code p
  are then ~p + g(e) for e = 0, e₁, e₂, that is `~p`, `1-p`, `B-p`, from
  either sublattice: from an even site this is ~g(a − e), from an odd site
  g(c + e). The `~` carries the sign change of the steps, so the walk needs
  no parity bookkeeping. This is the diamond code of
  [A001394](../A001394/) with one direction fewer.
- The code is exact on every walk. 2 and B+1 are even, so even sites get
  even codes and odd sites odd ones. Inside one sublattice
  g(a) = (2a₁ + a₂) + B·a₂, and a step changes one coordinate by 1, so two
  points k ≤ n steps apart have |Δa₁| + |Δa₂| ≤ n and |2Δa₁ + Δa₂| ≤ 2n < B.
  g(Δ) = 0 then gives B | 2Δa₁ + Δa₂, hence 2Δa₁ + Δa₂ = 0, then
  B·Δa₂ = 0, so Δa₂ = 0 and Δa₁ = 0. So `S`, a set of integers, is an exact
  visited set.
- B = 2n + 1 (it starts at 1 and goes up by 2 per term). `f(p,S)` counts the
  ways to finish a walk standing at p with visited set S; the walk is
  complete when it has n + 1 points, i.e. when `B<len(S)*2`, and then scores
  `True`. `+` prints a(0)'s `True` as 1.

**Golf notes**

- A brick-wall picture (x ± 1, and y + 1 or y − 1 by the parity of x + y)
  needs the parity in the code, `{p+1,p-1,p+B-p%2*2*B}`; the `~` coding
  hides it.
- The two sublattices must not share codes: with g(e₁) = 1 instead of 2 the
  origin and its neighbour at c = −e₁ would both get the code 0.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 1.85ⁿ, the connective
  constant √(2 + √2) of Duminil-Copin and Smirnov): a(22) comes after
  about 13 reference seconds and a(23) after about 25.
- The b-file has 106 terms (a(0) to a(105), Pfoertner's table); the bar is
  24 terms (up to a(23)) in 120 s, because a table of the first 23 terms
  would still fit in the program's 96 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 96 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001668), CC BY-SA 4.0.
