# A001335

> Number of n-step polygons on hexagonal lattice.
> — [OEIS A001335](https://oeis.org/A001335)

Offset 0: 1, 0, 0, 12, 24, 60, 180, 588, 1968, 6840, …

A polygon here is a self-avoiding walk from the origin back to the origin
on the triangular lattice (OEIS calls it hexagonal: every point has 6
neighbours): n steps through n distinct points, the last step closing the
loop. Polygons are counted with their starting point at the origin and with
a direction, so the 6 triangles at the origin, each run both ways, give
a(3) = 12; a(0) = 1 is the empty walk, and a(1) = a(2) = 0 because a
closed walk of one or two steps would repeat a point or an edge.

### Python 3 — 134 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for d in D if{w:=p+d}-S)if len(S)<B else B-2and p in D
B=0
while 1:D=1,-1,B,-B,B+1,~B;print(+f(0,{0}));B+=1
```

**How it works**

- The lattice is the one of [A001334](../A001334/): Z² with the six steps
  ±(1, 0), ±(0, 1), ±(1, 1), a point (i, j) stored as i + jB, so the step
  codes are `D=1,-1,B,-B,B+1,~B` (`~B` is −(B + 1)). A point (i, j) is
  |i| + |j| steps from the origin when i and j have opposite signs and
  max(|i|, |j|) otherwise; i + jB = 0 with j ≠ 0 forces the opposite sign
  and |i| ≥ B, so the only code 0 within B steps of the origin is the
  origin itself.
- For n ≥ 3, a(n) is the number of (n − 1)-step self-avoiding walks from
  the origin that end next to it: the n-th step closes the polygon, and the
  n − 1 points before it are distinct and avoid the origin.
- Here B = n. `f(p,S)` extends the walk, with the origin in S from the
  start, until it has n points (n − 1 steps, fewer than B, so the codes in
  S are exact as in A001334), then tests whether p is a neighbour of the
  origin: `p in D`. That test is exact too: if p had the code of a
  neighbour q, then p − q would have code 0 and lie within (n − 1) + 1 = B
  steps, so p = q.
- n ≤ 2: for B = 0 the walk is complete at once with p = 0, and D holds
  B = 0, so a(0) = `True`; for B = 1, D = (1, −1, 1, −1, 2, −2) has no 0,
  so a(1) = `False`; for B = 2 the closing step could only retrace the
  first one, and `B-2and` makes the score 0. `+` prints the booleans as 1
  and 0.

**Golf notes**

- The end test needs the start in S (so that walks through the origin
  are excluded) and a short "next to the origin". With the pairs
  `for d in(1,B,~B)for w in{p+d,p-d}-S` of A001334 and the test
  `abs(p)in(1,B,B+1)` it is 137 bytes.
- The steps ±1, ±B, ±(B − 1) (the differences of `U=0,1,B`, as in
  [A000765](../../A000xxx/A000765/)) would not do at B = n: the point
  (1 − B, 1) is then n − 1 steps away and has the code 1 of a neighbour.
- Closing the walk with one more step instead, as in the short-bar record
  below, is 11 bytes shorter but enumerates n-step instead of
  (n − 1)-step walks.

**Notes**

- Exhaustive depth-first search over all (n − 1)-step self-avoiding walks
  with exact integer arithmetic, so it is correct for every n. Each step
  adds two frames (the lambda and its generator), so Python's default
  recursion limit of 1000 would only matter near n = 490; memory stays tiny.
- The time grows like the number of walks (about 4.15ⁿ): a(11) comes
  after about 11 s and a(12) after about 45 s here (about 26
  reference seconds).
- The b-file is synthesized from the OEIS data (27 terms, a(0) to a(26));
  the bar is 13 terms (up to a(12)) in 120 s.

## First 11 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(10) have to arrive in time.

### Python 3, 11 terms — 123 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for d in(1,B,~B)for w in{p+d,p-d}-S)if len(S)<B else 0==p!=B-3
B=1
while[print(+f(0,{.5}))]:B+=1
```

**How it works**

- Same lattice and code as above, with the steps written as pairs
  `for d in(1,B,~B)for w in{p+d,p-d}-S` as in A001334 (no D is needed
  here). S starts as `{.5}`, a placeholder
  that no integer code equals: the origin is not in S, so the walk may
  step back onto it, and `len(S)` counts the points after the start. B is
  n + 1, so the walk is complete after n steps.
- The points after the start are distinct (they are all in S), so a walk
  that ends at the origin after exactly n steps (`0==p`) visited it only at
  the ends: it is a closed self-avoiding walk. The walk has n < B steps,
  so S and the test p = 0 are exact as above.
- The only closed walk that is not a polygon is the step out and back for
  n = 2, B = 3: `!=B-3` drops it. a(0) (B = 1) is the empty walk, p = 0,
  scored `True`; a(1) can never end at the origin.

**Limits**

- It enumerates all n-step walks instead of the (n − 1)-step ones, so
  each term takes about 4–5 times as long as with the main record: a(10)
  comes after about 14 s here (about 7 reference seconds), and a(11) after
  about 73 s (45 reference seconds), too close to the limit of 60 for a
  12-term bar.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 134 | first entry |
| 2026-11-09 | Python 3, 11 terms | 123 | first entry: close the walk with one more step |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001335), CC BY-SA 4.0.
