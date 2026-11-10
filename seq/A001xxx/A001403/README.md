# A001403

> Number of combinatorial configurations of type (n_3).
> — [OEIS A001403](https://oeis.org/A001403)

Offset 1: 0, 0, 0, 0, 0, 0, 1, 1, 3, 10, 31, 229, 2036, …

An (n_3) configuration has n points and n lines, each line a set of three
points, each point on three lines, and two lines never share more than one
point. a(n) counts them up to isomorphism (relabelling the points); the
Fano plane is the only (7_3).

### Python 3 — 460 bytes

```python
from itertools import*
def g(L):
 F=sum(L,())
 if len(L)==n:S.add(min(sum(1<<sum(1<<(p,*q,*r).index(v)for v in l)for l in L)for p in R for q in permutations({*sum([l for l in L if p in l],())}-{p})for r in permutations({*R}-{p,*q})))
 for l in combinations(R,3):
  if l>L[-1]and sum(v<l[0]for v in F)==3*l[0]and max(len({*l}&{*m})for m in L)<2>max(map(F.count,l))-1:g(L+[l])
n=0
while n:=n+1:R=range(n);S=set();n>6and g([(0,1,2),(0,3,4),(0,5,6)]);print(len(S))
```

**How it works**

- The three lines through a point p meet only at p, so they hold
  1 + 3·2 = 7 different points: there is no configuration with n < 7
  (`n>6and`), and every configuration can be relabelled so that the lines
  through point 0 are {0,1,2}, {0,3,4}, {0,5,6}. The search starts from
  them.
- Lines are sorted triples, added in increasing order (`l>L[-1]`), and
  each new line starts at the smallest point that still lies on fewer than
  three lines: `sum(v<l[0]for v in F)==3*l[0]` says every point below
  l[0] is already on three lines (F lists all incidences). Every
  configuration is reached this way, its lines in sorted order: the next
  line can't start lower (that point would be full) or higher (the
  smallest unfinished point could never be finished). A new line must
  meet each old one in at most one point and add only points on fewer
  than three lines. With n lines, 3n incidences and at most three per
  point, every point is on exactly three.
- Each finished configuration gets a canonical form: relabel it by an
  order o = (p, the six points collinear with p in any order, the other
  points in any order), point v becoming `o.index(v)`, encode the result
  as an integer (a line is the bit mask m of its points, the
  configuration Σ 2^m over its lines, so the code determines the lines)
  and take the smallest code over all such orders. The orders are defined
  by the configuration alone, so isomorphic configurations get the same
  minimum, and the minimum is the code of a relabelling, so equal forms
  mean isomorphic. a(n) is the number of different forms, `len(S)`.
- `if len(L)==n` needs no `else`: on a full configuration every point is
  on three lines, so no further line passes the test.

**Notes**

- Correct for every n: an exhaustive search with an exact isomorphism
  test, no theorem needed.
- The b-file is synthesized from the OEIS data (20 terms, n = 1 to 20);
  the bar is 9 terms (up to a(9) = 3) in 120 s. a(9) comes after about
  56 s here: 176 normalized configurations of 9 points, each tried in
  9·720·2 orders. a(10) has 5952 of them and 10·720·6 orders each,
  about a hundred times more work.
- Taking only the 48 orders that keep p's lines together (the six points
  in pairs) is 15 times faster but about 60 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 460 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001403), CC BY-SA 4.0.
