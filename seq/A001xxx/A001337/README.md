# A001337

> Number of n-step polygons on f.c.c. lattice.
> — [OEIS A001337](https://oeis.org/A001337)

Offset 1: 0, 0, 48, 264, 1680, 11640, 86352, 673104, 5424768, 44828400, …

A polygon here is a closed self-avoiding walk on the face-centred cubic
lattice (12 neighbours (±1, ±1, 0) and permutations) starting at the
origin: n steps through n distinct points, the last step returning to the
origin. Polygons are counted with their starting point at the origin and
with a direction: two neighbouring points have 4 common neighbours, so
a(3) = 12·4 = 48 triangles. a(1) = a(2) = 0 because a closed walk of one or
two steps would repeat a point or an edge.

### Python 3 — 155 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for d in D if{w:=p+d}-S)if len(S)<B else B>2and p in D
B=1
while[print(+f(0,{0}))]:B+=1;D={B**(i%4)-B**(i//4)for i in range(16)}
```

**How it works**

- The f.c.c. lattice is the root lattice A₃: the points c ∈ Z⁴ with
  c₁ + c₂ + c₃ + c₄ = 0, joined by the 12 vectors eᵢ − eⱼ (the map
  c ↦ (c₁ + c₂, c₁ + c₃, c₁ + c₄) sends these onto the 12 vectors
  (±1, ±1, 0)); a point is ½(|c₁| + |c₂| + |c₃| + |c₄|) steps from the
  origin. A point is stored as the integer c₁ + c₂B + c₃B² + c₄B³, so D,
  the set of all B^i − B^j for i, j < 4, holds the 12 step codes and 0
  (i = j). A step to w = p is never taken, since p is already in S.
- For n ≥ 3, a(n) is the number of (n − 1)-step self-avoiding walks from
  the origin that end next to it: the n-th step closes the polygon, and the
  n − 1 points before it are distinct and avoid the origin.
- Here B = n. `f(p,S)` extends the walk, with the origin in S from the
  start, until it has n points, then tests `p in D`.
- Both S and the test are exact, because no nonzero x within B steps of
  the origin has code 0 (B ≥ 2). Such an x has |xᵢ| ≤ B, and x₁ ≡ 0
  (mod B) gives x₁ ∈ {0, ±B}. If x₁ = ±B, the other three coordinates
  have the opposite sign (their sizes add up to B), and dividing the code
  by x₁ leaves 1 − (y₂ + y₃B + y₄B²) = 0 with yᵢ = |xᵢ|, so y₂ = 1,
  y₃ = y₄ = 0 and the sizes add up to 1, not B. If x₁ = 0, then
  x₂ ∈ {0, ±B}: x₂ = 0 leaves x₃ + x₄B = 0 and x₃ + x₄ = 0, so x = 0;
  x₂ = ±B forces x₃ and x₄ to the opposite sign with
  x₂/B + x₃ + x₄B = 0, so x₄ = 0, x₃ = ∓1 and x₂ + x₃ = ±(B − 1) ≠ 0,
  against the zero sum. Two points of the walk are at most n − 1 < B
  steps apart, and an end point p with the code of a neighbour q gives a
  p − q at most (n − 1) + 1 = B steps long, so p = q.
- n ≤ 2: `B>2and` scores 0 when the walk has one point (n = 1) or when the
  closing step could only retrace the first one (n = 2); `+` prints that
  `False` as 0. D is first needed for B = 2, so it is set in the loop body
  after printing a(1).

**Golf notes**

- With the codes `U=0,1,B,B*B` of [A000765](../../A000xxx/A000765/)
  (c₂ + c₃B + c₄B², c₁ left out) the walk is still exact, but the
  neighbour test is not: (2 − B, B − 1, −1, 0) is n − 1 steps away and
  has the code −1 of e₁ − e₂. The powers B⁰…B³ of all four coordinates
  close that gap; so does `U=0,-1,B,B**3`, but
  `U=0,-1,B,B**3;D={a-b for a in U for b in U}` is 3 bytes longer.
- Writing the steps as differences inside the lambda,
  `for a in U for b in U if{w:=p+a-b}-S` and
  `p in{a-b for a in U for b in U}`, costs 11 bytes more than building D.
- Closing the walk with one more step instead, as in the short-bar record
  below, is 22 bytes shorter but enumerates n-step instead of
  (n − 1)-step walks.

**Notes**

- Exhaustive depth-first search over all (n − 1)-step self-avoiding walks
  with exact integer arithmetic, so it is correct for every n. Each step
  adds two frames (the lambda and its generator), so Python's default
  recursion limit of 1000 would only matter near n = 490; memory stays tiny.
- The time grows like the number of walks (about 10ⁿ): a(7) comes after
  about 3 s and a(8) after about 25 s here (about 14 reference seconds).
- The b-file is synthesized from the OEIS data (18 terms, a(1) to a(18));
  the bar is 8 terms (up to a(8)) in 120 s.

## First 7 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(7) have to arrive in time.

### Python 3, 7 terms — 133 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for i in range(16)if{w:=p+B**(i%4)-B**(i//4)}-S)if len(S)<B else 0==p<B-3
B=2
while[print(f(0,{.5}))]:B+=1
```

**How it works**

- The code of [A001336](../A001336/): a point is c₁ + c₂B + c₃B² + c₄B³
  and a step is B^a − B^b with a = i mod 4, b = ⌊i/4⌋. Here B = n + 1,
  and S starts as `{.5}`, a placeholder that no integer code equals: the
  origin is not in S, so the walk may step back onto it, and `len(S)`
  counts the points after the start, so the walk is complete after n
  steps. The loop starts at B = 2, the offset n = 1.
- The points after the start are distinct (they are all in S), so a walk
  that ends at the origin after exactly n steps (`0==p`) visited it only at
  the ends: it is a closed self-avoiding walk. It has n < B steps, so every
  coordinate difference is below B, the base-B code is exact and so is
  the test p = 0.
- The steps a = b (w = p) are blocked by S except at the very first step,
  where they put the walk on the origin for good: such a walk can only
  count for n = 1. That case (B = 2) and the step out and back for n = 2
  (B = 3) are the only closed walks that are not polygons, and `<B-3`
  drops both, so every printed value is an integer.
- The main record's precomputed D is 18 bytes longer here, and the
  differences `a-b` of `U=0,1,B,B*B` 2 bytes longer (they need U before
  the first term).

**Limits**

- It enumerates all n-step walks instead of the (n − 1)-step ones, so
  each term takes about ten times as long as with the main record:
  a(7) comes after about 49 s here (about 32 reference seconds), and a(8)
  would need about ten times that, far beyond the limit of 60.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 155 | first entry |
| 2026-11-09 | Python 3, 7 terms | 133 | first entry: close the walk with one more step |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001337), CC BY-SA 4.0.
