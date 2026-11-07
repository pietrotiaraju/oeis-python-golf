# A000759

> Number of n-step self-avoiding walks on cubic lattice ending at point with x=0.
> — [OEIS A000759](https://oeis.org/A000759)

Offset 0: 1, 4, 12, 44, 172, 772, 3308, 14924, 64956, 294252, …

The walks live on the simple cubic lattice Z³ (6 neighbours ±e₁, ±e₂,
±e₃), start at the origin and are counted by the signed x-coordinate of the
end point, here x = 0. The siblings [A000760](../A000760/), [A000761](../A000761/), [A000762](../A000762/) take the other
values of x with the same template.

### Python 3 — 119 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B else p%B<1
B=1
while[print(+f(0,{0}))]:B+=1
```

**How it works**

- A point (x, y, z) is stored as the integer x + yB + zB², so the six
  steps are ±1, ±B, ±B²: `for d in(1,B,B*B)for w in{p+d,p-d}-S`, where the
  set difference keeps the unvisited neighbours w with no walrus or `if`.
- B = n + 1.
  Two points of an n-step walk are at most n steps apart, so each
  coordinate differs by at most n < B: the encoding is injective on every
  walk and `S`, a set of integers, is an exact visited set.
- `f(p,S)` counts the ways to finish a walk that stands at p with visited
  set S. The walk is complete when it has n + 1 points, i.e. when
  `len(S)<B` fails; it then scores 1 if p ≡ 0 (mod B).
- The walk starts at p = 0 and p ≡ x (mod B); since |x| ≤ n < B,
  `p%B<1` means x = 0 exactly. `+` prints a(0) = `True` as 1.

**Golf notes**

- Writing the six steps out with a walrus test,
  `for d in(1,-1,B,-B,B*B,-B*B)if{w:=p+d}-S`, is 4 bytes longer than
  building `{p+d,p-d}` per axis.
- With B = 2n + 1 the length test would be `len(S)*2<B`; the shift
  B = n + 1 makes it `len(S)<B`, 2 bytes shorter.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 4.68ⁿ): a(10) comes after about 22 s and a(11) after about 100 s here, the same for every x.
  [A000765](../A000765/)–[A000768](../A000768/) (f.c.c. lattice) use the same method.
- The b-file is synthesized from the OEIS data (23 terms, up to
  a(22)); the bar is 11 terms (up to a(10)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 119 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000759), CC BY-SA 4.0.
