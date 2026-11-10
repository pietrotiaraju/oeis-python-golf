# A001411

> Number of n-step self-avoiding walks on square lattice.
> — [OEIS A001411](https://oeis.org/A001411)

Offset 0: 1, 4, 12, 36, 100, 284, 780, 2172, 5916, 16268, …

A self-avoiding walk on the square lattice starts at the origin, makes n
unit steps and never visits a point twice. a(n) counts these walks (all
directions, no symmetry reduction). The siblings
[A001412](../A001412/) (cubic lattice) and [A001334](../A001334/)
(triangular lattice) use the same search.

### Python 3 — 100 bytes

```python
f=lambda p,S:B<=len(S)or sum(f(w,S|{w})for w in{p+1,p-1,p+B,p-B}-S)
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- B = n + 1 (it starts at 1 and grows by one per term). The point (x, y) is
  the integer x + yB, so the four neighbours of p are `p+1`, `p-1`, `p+B`,
  `p-B`, and `{...}-S` drops the visited ones.
- Exactness of the code: two points of an n-step walk are at most n steps
  apart, so |Δx| + |Δy| ≤ n < B. Equal codes mean Δx = −B·Δy, which for
  Δy ≠ 0 needs |Δx| ≥ B. So the code is one-to-one on every walk and `S`, a
  set of integers, is an exact visited set.
- `f(p,S)` counts the ways to finish a walk standing at p with visited set
  S. A walk is complete when it has n + 1 points, `B<=len(S)`, and then
  scores `True`; `+` prints a(0)'s bare `True` as 1.

**Golf notes**

- The four neighbours written out, `{p+1,p-1,p+B,p-B}`, are shorter than a
  direction loop `for d in(1,B)for w in{p+d,p-d}`.
- Coding the two sublattices with opposite signs (neighbours `~p`, `1-p`,
  `B-p`, `-B-p`) also works but saves nothing here.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator); the default recursion limit would
  matter only near n = 490.
- The time grows like the number of walks (about 2.64ⁿ): a(15) comes after
  about 20 s and a(16) after about 55 s here.
- The b-file has 80 terms (a(0) to a(79), from Jensen's enumerations); the
  bar is 16 terms (up to a(15)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 100 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001411), CC BY-SA 4.0.
