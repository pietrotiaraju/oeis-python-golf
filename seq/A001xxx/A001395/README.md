# A001395

> Number of (2n+1)-step self-avoiding walks on diamond lattice ending at point with x = 1.
> — [OEIS A001395](https://oeis.org/A001395)

Offset 0: 2, 10, 74, 518, 3934, 29914, 232094, 1812890, 14277886, 113016230, …

The walks live on the diamond lattice (four neighbours per point; see
[A001394](../A001394/) for the code), start at the origin and are counted by
the Cartesian x coordinate of the end point, here x = 1, with the bonds
taken as (±1, ±1, ±1) as usual: with that scale every listed term matches.
The siblings [A001396](../A001396/), [A001397](../A001397/), [A001398](../A001398/) take the other values of x with the same template.

### Python 3 — 113 bytes

```python
f=lambda p,S:p%-~B<1if B<len(S)*2else sum(f(w,S|{w})for w in{~p,1-p,B-p,B*B-p}-S)
B=3
while[print(f(1,{1}))]:B+=4
```

**How it works**

- Same walk as [A001394](../A001394/): lattice coordinates over
  b₁ = (0, 2, 2), b₂ = (2, 0, 2), b₃ = (2, 2, 0), an odd base B, code
  g(a) = (B+1)a₁ + 2a₂ + (B²+1)a₃ for even sites and ~g(c) for odd sites, so
  the neighbours of p are `~p`, `1-p`, `B-p`, `B*B-p`. The code is exact on
  every s-step walk when B > 2s.
- Reading x: an even site a has x = 2a₂ + 2a₃ (b₁ has x = 0, b₂ and b₃ have
  x = 2), and B ≡ −1 (mod B + 1) gives g(a) ≡ 2a₂ + 2a₃ = x (mod B + 1). An
  odd site c has x = 2c₂ + 2c₃ + 1, so g(c) ≡ x − 1.
- Starting at the code p₀ instead of 0 gives even sites p₀ + g(a) and odd
  sites ~(p₀ + g(c)); the neighbour rule is the same and the parity
  argument still keeps the sublattices apart. The end code then satisfies
  p ≡ p₀ + x after an even number of steps and p ≡ −p₀ − x after an odd
  number (mod B + 1), so the leaf test `p%-~B<1` (−~B is B + 1) means
  x ≡ −p₀ in both cases.
- Here s = 2n + 1 and B = 4n + 3 (it starts at 3 and goes up by 4), p₀ = 1. The end point has |x + 1| ≤ 2n + 2 < 4n + 4, so p ≡ 0 (mod 4n + 4) means x = −1 exactly, which by the rotation below has the same count as x = 1.
- The rotation by π about the z axis, (x, y, z) ↦ (−x, −y, z), maps
  {v₀, v₁, v₂, v₃} onto itself (v₀ ↔ v₃, v₁ ↔ v₂), so it is a symmetry of the
  lattice fixing the origin, and it pairs the walks ending at x with those
  ending at −x.
- The walk is complete at s + 1 points, i.e. when `B<len(S)*2`, and
  `p%-~B<1if … else sum(…)` scores it.

**Golf notes**

- `p%-~B<1if B<len(S)*2else sum(…)` is 2 bytes under
  `sum(…)if len(S)*2<B else p%-~B<1`.
- Reading x modulo B itself needs the two x-raising steps to share a residue
  mod B, e.g. steps (0, 2, B+2, B²) with an even B: `{~p,1-p,B+1-p,B*B+~p}`
  and `p%B<1`, one byte longer in total.
- Starting at p₀ = 1 moves the target residue to 0, so all four siblings
  share the test `p%-~B<1`.

**Notes**

- Exhaustive depth-first search over all walks with exact integer
  arithmetic, so it is correct for every n; recursion depth and memory are
  as in [A001394](../A001394/).
- Each term adds two steps, about 8.3 times the work: a(7) comes after about 33 s and a(8) after about 4 minutes here.
- The b-file is synthesized from the OEIS data (16 terms, up to a(15));
  the bar is 8 terms (up to a(7)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001395), CC BY-SA 4.0.
