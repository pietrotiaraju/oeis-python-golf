# A000644

> Number of loops of length 4n on square grid that turn at each step and return to start in original direction.
> — [OEIS A000644](https://oeis.org/A000644)

Offset 1: 1, 1, 3, 7, 31, 138, 808, 4956, 33047, 227328, 1614793, 11710299, …

A loop is a closed walk of unit steps that turns left or right after every
step and never uses an edge twice (it may touch itself at a corner).
Rotations, reflections, translations, the starting point and the direction
of travel do not count (Sean A. Irvine's comment on the OEIS page). The
smallest loop after the unit square is two squares touching at a corner.

### Python 3 — 202 bytes

```python
from itertools import*
d=n=4
while[print(len({min(t[j:]+t[:j]for t in(t,t[::-1])for j in range(n))for t in product(*[(1,-1)]*n)if sum(t)+(p:=0)==4if len({p+(p:=p+(d:=d*1j*x))for x in t})-n==p*n}))]:n+=4
```

**How it works**

- **Turn sequences.** Up to rotation and translation a loop is its cyclic
  sequence t of turns, +1 left and −1 right; here n is the length 4k. A
  loop never crosses itself (a crossing would need a straight step), so it
  can be pulled apart into a simple closed curve and its turns add up to
  ±4. Reflection negates every turn, so each loop has a version with
  Σt = 4, and the only symmetries left are the cyclic shifts and the
  reversal of t (travelling backwards and reflecting). The canonical form
  is the least of those 2n sequences; the answer is the number of distinct
  canonical forms.
- **The walk.** The heading `d` turns by `1j*x` and then the position `p`
  moves by it; `p+(p:=p+d)` is old p plus new p, twice the midpoint of the
  edge just walked, which identifies the edge. A loop uses n distinct edges
  and ends at its start, so the test is `len({…})-n==p*n`: p is a multiple
  of 4 here, so p·n would be at least 4n in size if p were not 0.
- **Small resets.** `sum(t)+(p:=0)==4` also puts p back to 0. The heading
  needs no reset: with Σt = 4 the product of the n factors 1j·x is
  1j^n·(−1)^(n/2−2) = 1, so d is back to its start after every walk. Its
  start is 4 instead of 1, which only scales the picture and lets
  `d=n=4` set both.

**Notes**

- The complex numbers only hold points with integer coordinates below 8n
  in size, and they are only added and multiplied by ±1j, so every float
  operation on them is exact.
- Brute force over all 2^(4k) turn sequences: a(1) … a(5) print in about
  3 s, a(6) needs about 45 s more on this PC. The bar is 5 terms in 60 s. A
  depth-first search with pruning reaches a(8) = 4956 in under a minute
  and confirms this reading of the definition, but costs many more bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 202 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000644), CC BY-SA 4.0.
