# A001336

> Number of n-step self-avoiding walks on f.c.c. lattice.
> — [OEIS A001336](https://oeis.org/A001336)

Offset 0: 1, 12, 132, 1404, 14700, 152532, 1573716, 16172148, 165697044, 1693773924, …

The walks live on the face-centred cubic lattice (the integer points with
even coordinate sum; 12 neighbours (±1, ±1, 0) and permutations), start at
the origin and never visit a point twice.

### Python 3 — 120 bytes

```python
f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for i in range(16)if{w:=p+B**(i%4)-B**(i//4)}-S)
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- The f.c.c. lattice is the root lattice A₃: the points c ∈ Z⁴ with
  c₁ + c₂ + c₃ + c₄ = 0, joined by the 12 vectors eᵢ − eⱼ (the map
  c ↦ (c₁ + c₂, c₁ + c₃, c₁ + c₄) sends these onto the 12 vectors
  (±1, ±1, 0)). A point is stored as the integer
  c₁ + c₂B + c₃B² + c₄B³, so the steps are the differences B^a − B^b,
  with a = i mod 4 and b = ⌊i/4⌋ for i < 16. The four pairs a = b give
  w = p, which is already in S, so the self-avoidance test drops them too.
- B = n + 1. Each step changes every cᵢ by at most 1, so two points of an
  n-step walk differ by less than B in every coordinate, and a base-B
  number with digits of size below B is 0 only when every digit is 0
  (the lowest digit is ≡ 0 mod B, so it is 0; divide by B and repeat): the
  encoding is injective on every walk and `S`, a set of integers, is an
  exact visited set.
- `f(p,S)` counts the ways to finish a walk that stands at p with visited
  set S. The walk is complete when it has n + 1 points (`B<=len(S)`) and
  then scores `True`; otherwise it sums over the unvisited neighbours.
- a(0) needs no step; `+` prints its `True` as 1.

**Golf notes**

- The template of [A000765](../../A000xxx/A000765/) (walks ending at
  x = 0) without the end test, `U=0,1,B,B*B` and
  `for a in U for b in U if{w:=p+a-b}-S`, is 1 byte longer, and listing
  the six step pairs, `for d in(1,B,B*B,B-1,B*B-1,B*B-B)for w in{p+d,p-d}-S`
  as in [A001334](../A001334/), 5 bytes longer. The powers cost about a
  fifth more time than the precomputed U.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 10ⁿ): a(6) comes after
  about 3 s and a(7) after about 32 s here (about 20 reference seconds).
- The b-file has 25 terms (a(0) to a(24), from Schram, Barkema, Bisseling
  and Clisby); the bar is 8 terms (up to a(7)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001336), CC BY-SA 4.0.
