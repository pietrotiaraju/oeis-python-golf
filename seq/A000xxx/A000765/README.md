# A000765

> Number of n-step self-avoiding walks on f.c.c. lattice ending at point with x = 0.
> — [OEIS A000765](https://oeis.org/A000765)

Offset 0: 1, 4, 36, 308, 2764, 25404, 237164, 2237948, 21286548, 203701772, …

The walks live on the face-centred cubic lattice (the integer points with
even coordinate sum; 12 neighbours (±1, ±1, 0) and permutations), start at
the origin and are counted by the signed x-coordinate of the end point, here
x = 0. The siblings [A000766](../A000766/), [A000767](../A000767/), [A000768](../A000768/) take the other values of x with the
same template.

### Python 3 — 133 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for a in U for b in U if{w:=p+a-b}-S)if len(S)<B else p%B<1
B=1
while[print(+f(0,{0}))]:B+=1;U=0,-1,~B,B*B
```

**How it works**

- The f.c.c. lattice is the root lattice A₃: the points c ∈ Z⁴ with
  c₁ + c₂ + c₃ + c₄ = 0, joined by the 12 vectors eᵢ − eⱼ. The map
  c ↦ (c₁ + c₂, c₁ + c₃, c₁ + c₄) sends these onto the 12 vectors
  (±1, ±1, 0), so x = c₁ + c₂.
- e₁, e₂, e₃, e₄ are stored as the integers `U=0,-1,~B,B*B`, and a step is
  a − b for a, b in U: `for a in U for b in U`. The pairs a = b give w = p,
  which is already in S, so the self-avoidance test drops them too (no
  `if a-b`).
- Modulo B, −1 and ~B = −B − 1 are both −1, and 0 and B² are both 0, so
  every step moves p mod B by minus its x-change: p ≡ p₀ − x (mod B). A
  point is (−x) + (−c₂)·B + c₃·B² away from the start, and each of x, c₂, c₃
  changes by at most 1 per step; with B = n + 1 > n
  the encoding is injective on every n-step walk, so `S` is an exact
  visited set.
- `f(p,S)` counts the ways to finish a walk that stands at p with visited
  set S; the walk is complete when `len(S)<B` fails (n + 1 points) and then
  scores 1 if p ≡ 0 (mod B).
- The walk starts at p = 0, so `p%B<1` means x ≡ 0 (mod B), and |x| ≤ n < B
  makes it exact. a(0) needs no step, so U is first set in the loop body,
  after printing it; `+` prints `True` as 1.

**Golf notes**

- The 12 Cartesian steps written out,
  `for a in(1,-1,B,-B)for b in(B,-B,B*B,-B*B)if a*a<b*b if{w:=p+a+b}-S`,
  cost 17 bytes more than the A₃ differences; writing the tuple U twice
  inside the lambda instead of the global costs 6 more.
- With B = 2n + 1 the length test would be `len(S)*2<B`; the shift
  B = n + 1 makes it `len(S)<B`, 2 bytes shorter.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 10ⁿ): a(6) comes after about 3 s and a(7) after about 35 s here, the same for every x.
  [A000759](../A000759/)–[A000762](../A000762/) (cubic lattice) use the same method.
- The b-file is synthesized from the OEIS data (16 terms, up to
  a(15)); the bar is 7 terms (up to a(6)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 133 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000765), CC BY-SA 4.0.
