# A000438

> Number of 1-factorizations of complete graph K_{2n}.
> — [OEIS A000438](https://oeis.org/A000438)

Offset 1: 1, 1, 6, 6240, 1225566720, 252282619805368320, 98758655816833727741338583040, …

### Python 3 — 311 bytes

```python
from functools import*
def M(V):
 if not V:yield 0
 else:
  a,*W=V
  for b in W:
   for e in M([x for x in W if x!=b]):yield e|1<<(b*(b-1)//2+a)
n=2
while 1:
 L=list(M(range(n)))
 @cache
 def F(E):
  if not E:return 1
  p=E&-E
  return sum(F(E^x)for x in L if x&p and x&E==x)
 print(F((1<<(n*(n-1)//2))-1));n+=2
```

**How it works**

- A 1-factor is a perfect matching: every vertex belongs to one
  selected edge. A 1-factorization partitions all edges of K_n
  into n−1 such matchings. Vertices are labeled, while the
  collection of factors is unordered. The code's n is twice
  the OEIS index.
- M(V) pairs the least remaining vertex a with each possible
  partner b and recursively pairs the rest. Each matching has
  exactly one such first pair, so this generates all (n−1)!!
  perfect matchings once.
- Edge {a,b}, with a<b, occupies bit b(b−1)/2+a. The blocks
  for successive larger endpoints fill positions 0 through
  C(n,2)−1, so `(1<<(n*(n-1)//2))-1` is the complete edge mask.
- F(E) counts factorizations of the remaining edge set. The empty
  set has one empty factorization. Otherwise `p=E&-E` isolates
  its least edge; consider only matching masks x containing p
  and lying wholly in E.
- `x&E==x` is the subset test. Under that condition `E^x`
  removes exactly x's edges, and the recursive count covers the
  rest. If no matching fits, the empty sum gives zero.
- Every factorization contains exactly one matching covering the
  chosen least edge. Repeating this rule gives it a unique order
  of removal, so factor permutations are not overcounted.

**Notes**

- `@cache` shares repeated remaining-edge subproblems. F is
  redefined for each graph size, so cached values never mix two
  different edge encodings or matching lists.
- This is an exact-cover count with exact integer masks and sums.
  Its recursion has n−1 matching-removal levels, but the number
  of reachable masks can be very large.
- [A000474](../A000474/) further identifies factorizations
  under vertex relabeling. For K₆ this page counts six labeled
  factorizations, all in its single isomorphism class; for K₈
  the counts are 6240 and six respectively.
- [A000479](../A000479/) uses the same least-edge recurrence
  for complete bipartite graphs, with a different matching generator.
- The b-file has 7 terms (indices 1 through 7). The bar is the
  first 4 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 311 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000438), CC BY-SA 4.0.
