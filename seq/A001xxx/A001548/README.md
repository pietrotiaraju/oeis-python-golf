# A001548

> Number of connected linear spaces with n (unlabeled) points.
> — [OEIS A001548](https://oeis.org/A001548)

Offset 0: 1, 1, 0, 1, 1, 2, 4, 13, 42, 308, 4845, 227613, 28639650

A linear space on n points is a family of lines, each with at least two
points, such that every pair of points lies on exactly one line (the
spaces of [A001200](../A001200/)). Following Michael Somos's comment on
the entry, it is **disconnected** when its points split into two
nonempty parts such that the line through two points of the same part
lies inside that part; a(n) counts the connected ones up to relabelling.
The known terms come from computer enumerations; a short program can
only generate and compare up to isomorphism.

**Connected means: the lines of three or more points link all points.**
If some part A (and its complement B) is closed in the sense above, a
line with ≥ 3 points has two of them in the same part and so lies inside
it: no such line meets both parts. Conversely, if the lines of ≥ 3
points split the points into several linked groups, take A = one group:
the line through two points of A is either a 2-point line (inside A) or
a big line through a point of A (inside A, by the choice of A), and the
same holds for B. So a space is connected exactly when the graph "two
points share a line of ≥ 3 points" is connected. This gives the data's
small values: a(1) = 1 (one point), a(2) = 0 (two points, one 2-point
line), and a(0) = 1 with the empty space counted as connected, as in
the data. Somos also notes that A001200 is the Euler transform of this
sequence, which is the same statement: a space is the disjoint union of
its linked groups, joined by 2-point lines.

### Python 3 — 412 bytes

```python
from itertools import*
L=[frozenset()];R=[];b=1
while[print(sum(c>b-2for e in L if[c:=1%b]+[c:=c|l for l in[*e]*b if l&c>0<l.bit_count()-2]))]:
 W={X|{u|b for u in R}for X in L};R+=b,;Q=[*zip(*permutations(R))]
 for l in range(b):T={l}|{u|b for u in R if l&u};W|={w-T|{l|b}for w in W if T<=w}
 L=[e for e in[*W]if e in W!={*map(W.discard,map(set,zip(*[map(sum,zip(*[q for q in Q if m&q[0]]))for m in e])))}];b*=2
```

**How it works**

- The generator is [A001200](../A001200/)'s main record, unchanged: `L`
  holds one labelled space per isomorphism class on the points so far
  (points are the powers of two in `R`, lines are bitmasks, a space is
  the frozenset of all its lines). See that page for why every class
  is found exactly once: every space on n points is a space on n − 1
  points plus a new point on some pairwise disjoint old lines, and
  whole orbits under all n! relabellings are removed from the candidate
  set.
- Only the count changes. For each space `e`, `c` starts as the first
  point (`1%b`, which is 0 for the empty space, b = 2ⁿ). The lines are
  scanned b ≥ n times (`[*e]*b`) and each line with ≥ 3 points
  (`l.bit_count()-2>0`) that meets `c` (`l&c>0`) is merged into `c`;
  every scan that changes anything adds a point, so n scans reach the
  closure. The space is connected when `c` holds all n points, b − 1:
  `c>b-2`. The scan sits in the generator's `if`: `[c:=1%b]+[…]` is a
  nonempty list, so it always passes, after which `c>b-2` is evaluated
  and `sum` counts the connected spaces.

**Notes**

- Exact set arithmetic, no theorem beyond the point-deletion argument
  of A001200 and the lemma above.
- The cost is a(n)·n! images as in A001200: a(8) = 42 comes after about
  11 s here (about 6 reference seconds); a(9) would need 384·9! images (minutes). Memory stays
  under 100 MB.
- The b-file has the 13 known terms; the bar is 9 terms in 60 s.

## First seven terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(6) have to arrive in time.

### Python 3, 7 terms — 318 bytes

```python
from itertools import*
n=0;C=combinations
while 1:R=range(n);print(len({min(sum(1<<sum(1<<p[i]for i in t)for t in T)for p in permutations(R))for k in range(1<<n)for T in C(C(R,3),k)if all({*C(sorted(S),3)}<={*T}for t,u in C(T,2)if len(S:={*t,*u})<5)and[c:={*R[:1]}]+[c:=c|{*t}for t in T*n if c&{*t}]and c=={*R}}));n+=1
```

**How it works**

- A001200's short-bar record: a linear space is the same thing as its
  set T of collinear triples, and a set of triples T comes from a space
  exactly when any two triples of T that share two points have all four
  triples of their union in T (proof on [A001200](../A001200/)'s page).
  The program runs over every subset T of the C(n, 3) triples, keeps
  those with this property, and counts them up to relabelling by the
  minimum over all n! relabellings of the triple-set bitmask.
- Added: the connectivity test, on the triples. Two points of a line
  with ≥ 3 points always lie in a common triple of T, and a triple of
  T lies on one line; so the triples link the same points as the big
  lines. `c` starts as `{*R[:1]}` (point 0, or nothing when n = 0), the
  triples are scanned n times (`T*n`) and each one meeting `c` is merged;
  the space is connected when `c=={*R}`. The cheaper linear-space test
  runs first.

**Limits**

- a(6) checks all 2²⁰ ≈ 10⁶ sets of triples on six points; the seven
  terms arrive in about 5 s here (under 3 reference seconds). a(7) would check 2³⁵ sets: out of
  reach. The main record builds the spaces point by point and reaches
  nine terms.
- Exhaustive and exact, so the program is right for every n; it is
  only slow.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-10 | 412 | first entry: A001200's generator, counting the connected spaces |

**Python 3, 7 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-10 | 318 | first entry: collinear triple sets, minimum over relabellings, connectivity on the triples |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001548), CC BY-SA 4.0.
