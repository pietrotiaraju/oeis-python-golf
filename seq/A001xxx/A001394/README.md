# A001394

> Number of n-step self-avoiding walks on diamond.
> — [OEIS A001394](https://oeis.org/A001394)

Offset 0: 1, 4, 12, 36, 108, 324, 948, 2796, 8196, 24060, …

The diamond lattice: every point has four neighbours, and the points form
two face-centred cubic lattices pushed apart by (1, 1, 1). The walks start at
a point and never visit a point twice. The siblings
[A001395](../A001395/)–[A001398](../A001398/) sort the same walks by the x
coordinate of the end point and use the same code.

### Python 3 — 102 bytes

```python
f=lambda p,S:B<len(S)*2or sum(f(w,S|{w})for w in{~p,1-p,B-p,B*B-p}-S)
B=1
while[print(+f(0,{0}))]:B+=2
```

**How it works**

- In Cartesian coordinates the even sites are the points with all coordinates
  even and x + y + z ≡ 0 (mod 4), the odd sites are the even sites plus
  (1, 1, 1). An even site steps by v₀ = (1, 1, 1), v₁ = (1, −1, −1),
  v₂ = (−1, 1, −1), v₃ = (−1, −1, 1), an odd site by their negatives.
- Lattice coordinates: b_t = v₀ − v_t, i.e. b₁ = (0, 2, 2), b₂ = (2, 0, 2),
  b₃ = (2, 2, 0), span the even sites. Write an even site as
  a₁b₁ + a₂b₂ + a₃b₃ and an odd site as c₁b₁ + c₂b₂ + c₃b₃ + v₀; then even
  site a and odd site c are neighbours exactly when c = a or c = a − e_t.
- Code, with an odd base B: g(a) = (B+1)a₁ + 2a₂ + (B²+1)a₃; an even site a
  gets g(a), an odd site c gets ~g(c) = −1 − g(c). The four neighbours of
  the code p are then ~p + g(e) for e = 0, e₁, e₂, e₃, that is `~p`, `B-p`,
  `1-p`, `B*B-p`, from either sublattice: from an even site this is
  ~g(a − e), from an odd site g(c + e). The `~` carries the sign change of
  the steps, so the walk needs no parity or sign bookkeeping.
- The code is exact on every walk. B odd makes B+1, 2 and B²+1 even, so even
  sites get codes of one parity and odd sites the other. Inside one
  sublattice g(a) = (a₁ + 2a₂ + a₃) + B·a₁ + B²·a₃, and a step changes one
  coordinate by 1, so over an n-step walk a₁ + 2a₂ + a₃ varies by at most 2n
  and a₁ by at most n. With B > 2n, g(Δ) = 0 gives Δ(a₁ + 2a₂ + a₃) ≡ 0
  (mod B), hence = 0, then Δa₁ + B·Δa₃ = 0, hence Δa₁ = Δa₃ = 0 and Δa₂ = 0.
  So two points of a walk share a code only if they are equal, and `S`, a
  set of integers, is an exact visited set.
- B = 2n + 1 (it starts at 1 and goes up by 2 per term). `f(p,S)` counts the
  ways to finish a walk standing at p with visited set S; the walk is
  complete when it has n + 1 points, i.e. when `B<len(S)*2`, and then scores
  `True`. `+` prints a(0)'s `True` as 1.

**Golf notes**

- Plain Cartesian codes x + yB + zB² need the step sign to alternate (a third
  argument or the parity of `len(S)`); `~p` absorbs it. The basis above makes
  the four neighbours `k-p` with k ∈ {−1, 1, B, B²}, the cheapest such set:
  the obvious steps (0, 2, B, B²) with an even B,
  `for d in(0,2,B,B*B)for w in{~p+d}-S`, cost 5 bytes more.
- The common factor 2 in g(e) is what keeps the sublattices apart: with
  g(e) = (1, B, B²) the origin and its neighbour v₁ would both get code 0.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 2.88ⁿ): a(15) comes after
  about 39 s and a(16) after about 2 minutes here.
- The b-file has 33 terms (a(0) to a(32), from Manyama's table); the bar is
  16 terms (up to a(15)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 102 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001394), CC BY-SA 4.0.
