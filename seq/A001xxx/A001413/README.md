# A001413

> Number of 2n-step self-avoiding cycles on the cubic lattice.
> — [OEIS A001413](https://oeis.org/A001413)

Offset 1: 0, 24, 264, 3312, 48240, 762096, 12673920, 218904768, 3891176352, 70742410800, …

a(n) counts the closed self-avoiding walks of 2n steps on the simple cubic
lattice that start and end at the origin: different step sequences count
as different, even when they trace the same polygon. Each polygon with 2n
edges (counted up to translation in [A001409](../A001409/)) is traced by 4n
of them: 2n choices of the vertex at the origin times 2 directions, all
different step sequences because a finite polygon is not invariant under a
nonzero translation (the OEIS formula a(n) = 4n·A001409(n)).

### Python 3 — 121 bytes

```python
f=lambda p,S:p==0<B^2if B<len(S)else sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)
B=2
while[print(f(0,{.5}))]:B+=2
```

**How it works**

- B = 2n (it starts at 2 and grows by 2 per term). The point (x, y, z)
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

**Golf notes**

- The placeholder `.5` in the start set lets one test, p = 0 at the end,
  close the walk; the alternative (origin in `S`, end next to it) needs a
  six-way neighbour test.
- `p==0<B^2` folds the n = 1 exception into the chained comparison; it is no
  longer than `p==0<B-2`.

**Notes**

- Exhaustive depth-first search over all 2n-step walks that never revisit a
  point other than the origin, with exact integer arithmetic, so it is
  correct for every n. The walks are not pruned when they are too far from
  the origin to return, which keeps the code short and the time about
  4.68²ⁿ: a(5) comes after about 22 s here and a(6) would take several
  minutes.
- The b-file has 16 terms (a(1) to a(16), the terms of the entry); the
  bar is 5 terms (up to a(5)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 121 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001413), CC BY-SA 4.0.
