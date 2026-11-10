# A001412

> Number of n-step self-avoiding walks on cubic lattice.
> — [OEIS A001412](https://oeis.org/A001412)

Offset 0: 1, 6, 30, 150, 726, 3534, 16926, 81390, 387966, 1853886, …

A self-avoiding walk on the simple cubic lattice starts at the origin,
makes n unit steps and never visits a point twice. a(n) counts these walks
(all directions). The square-lattice sibling is [A001411](../A001411/);
[A000761](../../A000xxx/A000761/) counts the walks of this search that end at
x = 2.

### Python 3 — 109 bytes

```python
f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- B = n + 1 (it starts at 1 and grows by one per term). The point
  (x, y, z) is the integer x + yB + zB², so the six neighbours of p are
  p ± d for d = 1, B, B², and `{p+d,p-d}-S` drops the visited ones.
- Exactness of the code: two points of an n-step walk are at most n steps
  apart, so |Δx| + |Δy| + |Δz| ≤ n < B. Equal codes mean
  Δx + BΔy + B²Δz = 0; then B divides Δx, so Δx = 0 (|Δx| < B), then
  Δy + BΔz = 0 gives Δy = 0 the same way, and Δz = 0. So the code is
  one-to-one on every walk and `S`, a set of integers, is an exact visited
  set.
- `f(p,S)` counts the ways to finish a walk standing at p with visited set
  S. A walk is complete when it has n + 1 points, `B<=len(S)`, and then
  scores `True`; `+` prints a(0)'s bare `True` as 1.

**Golf notes**

- Here the direction loop `for d in(1,B,B*B)for w in{p+d,p-d}` is shorter
  than the six neighbours written out.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n.
- The time grows like the number of walks (about 4.68ⁿ): a(10) comes after
  about 20 s and a(11) would take about 100 s here.
- The b-file has 37 terms (a(0) to a(36), from Schram, Barkema and
  Bisseling); the bar is 11 terms (up to a(10)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001412), CC BY-SA 4.0.
