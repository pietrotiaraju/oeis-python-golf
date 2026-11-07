# A000760

> Number of n-step self-avoiding walks on cubic lattice ending at point with x=1.
> — [OEIS A000760](https://oeis.org/A000760)

Offset 1: 1, 8, 40, 176, 748, 3248, 14280, 63768, 285296, 1285688, …

The walks live on the simple cubic lattice Z³ (6 neighbours ±e₁, ±e₂,
±e₃), start at the origin and are counted by the signed x-coordinate of the
end point, here x = 1, so a(n) = 0 below the offset. The siblings [A000759](../A000759/), [A000761](../A000761/), [A000762](../A000762/) take the other
values of x with the same template.

### Python 3 — 120 bytes

```python
f=lambda p,S:sum(f(w,S|{w})for d in(1,B,B*B)for w in{p+d,p-d}-S)if len(S)<B-1 else p%B<1
B=3
while[print(f(1,{1}))]:B+=1
```

**How it works**

- A point (x, y, z) is stored as the integer x + yB + zB², so the six
  steps are ±1, ±B, ±B²: `for d in(1,B,B*B)for w in{p+d,p-d}-S`, where the
  set difference keeps the unvisited neighbours w with no walrus or `if`.
- B = n + 2 (it starts at 3 and goes up by 1 per term).
  Two points of an n-step walk are at most n steps apart, so each
  coordinate differs by at most n < B: the encoding is injective on every
  walk and `S`, a set of integers, is an exact visited set.
- `f(p,S)` counts the ways to finish a walk that stands at p with visited
  set S. The walk is complete when it has n + 1 points, i.e. when
  `len(S)<B-1` fails; it then scores 1 if p ≡ 0 (mod B).
- The walk starts at p = 1, so p ≡ 1 + x (mod B). Since |x + 1| ≤ n + 1 < B,
  `p%B<1` means x = −1 exactly, which by the mirror x → −x has the same
  count as x = 1.

**Golf notes**

- Writing the six steps out with a walrus test,
  `for d in(1,-1,B,-B,B*B,-B*B)if{w:=p+d}-S`, is 4 bytes longer than
  building `{p+d,p-d}` per axis.
- With B = 2n + 1 the length test would be `len(S)*2<B`; the shift
  B = n + 2 makes it `len(S)<B-1`, the same length, with smaller integers.

**Notes**

- Exhaustive depth-first search over all n-step self-avoiding walks with
  exact integer arithmetic, so it is correct for every n. Each step adds two
  frames (the lambda and its generator), so Python's default recursion limit
  of 1000 would only matter near n = 490; memory stays tiny (one set per
  level).
- The time grows like the number of walks (about 4.68ⁿ): a(10) comes after about 22 s and a(11) after about 100 s here, the same for every x.
  [A000765](../A000765/)–[A000768](../A000768/) (f.c.c. lattice) use the same method.
- The b-file is synthesized from the OEIS data (22 terms, up to
  a(22)); the bar is 10 terms (up to a(10)) in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 120 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000760), CC BY-SA 4.0.
