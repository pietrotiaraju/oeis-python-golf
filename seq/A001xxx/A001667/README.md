# A001667

> 2n-step polygons on b.c.c. lattice.
> — [OEIS A001667](https://oeis.org/A001667)

Offset 2: 96, 1776, 43776, 1237920, 37903776, 1223681760, 41040797376, …

The body-centred cubic lattice: the points (x, y, z) with x, y, z all even
or all odd, each joined to its eight neighbours (x ± 1, y ± 1, z ± 1). As
the entry's comment says, the data count closed self-avoiding walks: walks
p₀ = 0, p₁, …, p₂ₙ = 0 with p₁, …, p₂ₙ distinct, rooted at the origin and
with a direction. a(2) = 96: each of the 8 first steps can be closed into a
square in 12 ways. (Each polygon with 2n edges is counted 2·2n times; the
lattice has no triangles, so the offset starts at 4 steps.)

### Python 3 — 128 bytes

```python
f=lambda p,S:sum(f(w,S|{w})if B>len(S)else w==0for d in(1,B,B*B,B*B-~B)for w in{p+d,p-d}-S)
B=4
while[print(8*f(1,{1,.5}))]:B+=2
```

**How it works**

- Lattice coordinates as in [A001666](../A001666/): with the basis
  e₁ = (1, 1, −1), e₂ = (1, −1, 1), e₃ = (−1, 1, 1) the eight steps are
  ±(1,0,0), ±(0,1,0), ±(0,0,1), ±(1,1,1), and c ↦ c₁ + c₂B + c₃B² turns
  them into `p±d` for d = 1, B, B², B² + B + 1 (`B*B-~B`).
- B = 2n (it starts at 4 and grows by 2 per term). The origin is not put
  into the visited set: `S` starts as `{1,.5}`, the first point p₁ = e₁
  (code 1) and a placeholder that no lattice point equals, so `len(S)` is
  the number of steps plus one. While the walk has fewer than 2n − 1 steps
  (`B>len(S)`) every unvisited neighbour w is entered; at 2n − 1 steps each
  unvisited neighbour scores `w==0`, the closing step onto the origin. A
  walk that passed through the origin earlier has it in `S` and cannot
  close, so exactly the closed self-avoiding walks are counted.
- The symmetries of the cube (all permutations and sign changes of x, y, z)
  map the lattice onto itself, fix the origin and carry any first step to
  any other, so every first step starts equally many closed walks: `8*`
  counts those starting with the step to e₁.
- Exactness of the code: the walks have at most 2n = B steps, so two of
  their points (the origin and the closing point included) are at most B
  steps apart, and each step changes each coordinate by at most 1. A nonzero
  Δc with all |Δcᵢ| ≤ B and Δc₁ + Δc₂B + Δc₃B² = 0 has Δc₁ ∈ {0, ±B}:
  Δc₁ = 0 leaves ±(0, B, −1), and Δc₁ = ±B leaves ±(B, −1, 0) or
  ±(B, B − 1, −1). Reaching Δc₁ = ±B (or Δc₂ = ±B) in at most B steps
  needs every step to move it by the same ±1, i.e. only steps ±(1,0,0)
  and ±(1,1,1) (or ±(0,1,0) and ±(1,1,1)) with one sign, and those never
  move another coordinate the other way; so none of these vectors is the
  difference of two points at most B steps apart.
  Hence the code is one-to-one where the walks go, `S` is exact, and
  `w==0` holds exactly at the origin.

**Golf notes**

- Scoring the closing step inside the generator (`…if B>len(S)else w==0`)
  costs the same as scoring at the end (`p==0if B<len(S)else sum(…)`), but
  stops one level earlier, about 7 times faster.
- `8*` and the start at e₁ cost 6 bytes and gain a factor 8 in time; that
  is what brings a(5) within the bar.

**Notes**

- Exhaustive depth-first search with exact integer arithmetic, so it is
  correct for every n; the default recursion limit would matter only near
  n = 245.
- The time grows like the number of (2n − 1)-step walks, about 6.5²ⁿ⁻¹:
  a(4) comes after under 2 s, a(5) after about 22 reference seconds
  (88 s on this busy machine), and a(6) would take some 40 times longer.
- The b-file has 10 terms (a(2) to a(11)); the bar is 4 terms (up to
  a(5)) in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 128 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001667), CC BY-SA 4.0.
