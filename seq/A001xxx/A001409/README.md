# A001409

> Number of 2n-step polygons on cubic lattice.
> — [OEIS A001409](https://oeis.org/A001409)

Offset 0: 1, 0, 3, 22, 207, 2412, 31754, 452640, 6840774, 108088232, …

a(n) counts the polygons with 2n edges on the simple cubic lattice, up to
translation (a(0) = 1 for the empty polygon). A polygon with 2n ≥ 4 edges
is traced by exactly 4n closed self-avoiding walks from the origin (2n
choices of the vertex at the origin, 2 directions; all different step
sequences, because a finite polygon is not invariant under a nonzero
translation), so a(n) = A001413(n)/(4n): the program counts those walks, as
[A001413](../A001413/) does, and divides.

### Python 3 — 132 bytes

```python
f=lambda p,S:p==0<B^2if B<len(S)else sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)
B=0
while[print(f(0,{.5})//(B*2or 1))]:B+=2
```

**How it works**

- B = 2n (it starts at 0 and grows by 2 per term). The point (x, y, z)
  is the integer x + yB + zB², and the six neighbours of p are p ± d for
  d = 1, B, B².
- The walk starts at the origin, but the origin is not put into the visited
  set: `S` starts as `{.5}`, a placeholder that no lattice point equals
  (it only shifts `len(S)` by one). So the walk may step back onto the
  origin, and `f(p,S)` scores 1 when, after 2n steps (`B<len(S)`), it
  stands at p = 0. Every other point is visited at most once, and the
  origin, once entered, is in `S`; so the scored walks are exactly the
  closed walks p₀ = 0, p₁, …, p₂ₙ = 0 with p₁, …, p₂ₙ distinct.
- For n = 1 that includes the six "cycles" that go out along one edge and
  straight back; they are not polygons, and `p==0<B^2` (p = 0 and
  0 < B XOR 2) is false exactly for B = 2. For n ≥ 2, p₁ and p₂ₙ₋₁ are
  different points of the walk, so its first and last edges differ and it
  traces a polygon with 2n edges.
- Exactness of the code: points of a 2n-step walk are at most 2n steps
  apart, so a nonzero lattice vector with code 0 would be needed between
  them; x + yB + zB² = 0 forces B | x, and then either x = 0 and y = −zB
  (|y| ≥ B), or |x| ≥ B with y or z nonzero; either way
  |x| + |y| + |z| ≥ B + 1 = 2n + 1. So no two points a walk can reach share
  a code, and in particular no point other than the origin has code 0.
- a(n) = (closed walks)/(4n) = (closed walks)/(2B). For n = 0 (B = 0) the
  root is already complete: p = 0 and 0 < 0 XOR 2, so the count is 1, and
  `B*2or 1` divides by 1 there instead of 0.

**Golf notes**

- Restricting the walk to codes ≥ 0 (filter `if-1<w`) makes the origin the
  lexicographically smallest vertex, so each polygon is found twice and
  `f(0,{.5})+1>>1` replaces the division. That is about five times faster
  but one byte longer, and a(6) would still take about 90 s here.

**Notes**

- Exhaustive depth-first search with exact integer arithmetic, so it is
  correct for every n. The time grows about like 4.68²ⁿ: a(5) comes after
  about 19 s here and a(6) would take several minutes.
- The b-file has 17 terms (a(0) to a(16), the terms of the entry); the bar
  is 6 terms (up to a(5)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 132 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001409), CC BY-SA 4.0.
