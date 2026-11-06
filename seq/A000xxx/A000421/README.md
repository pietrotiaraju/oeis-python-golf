# A000421

> Number of isomorphism classes of connected 3-regular (trivalent, cubic) loopless multigraphs of order 2n.
> — [OEIS A000421](https://oeis.org/A000421)

Offset 1: 1, 2, 6, 20, 91, 509, 3608, 31856, 340416, 4269971, …

### Python 3 — 596 bytes

```python
from itertools import*
def G(i,D):
 if i==n:
  V={0}
  for _ in R:V|={j for i in V for j in R if A[i][j]}
  if len(V)==n:yield tuple(A[i][j]for j in R for i in range(j))
 else:
  for U in combinations_with_replacement(range(i+1,n),D[i]):
   C=D*1
   for j in U:C[j]-=1
   if min(C[i+1:],default=0)<0:continue
   for j in range(i+1,n):A[i][j]=A[j][i]=U.count(j)
   C[i]=0;yield from G(i+1,C)
n=2
while 1:
 R=range(n);A=[[0]*n for _ in R];S=set();c=0
 for t in G(0,[3]*n):
  if t in S:continue
  c+=1
  for p in permutations(R):S.add(tuple(A[p[i]][p[j]]for j in R for i in range(j)))
 print(c);n+=2
```

**How it works**

Fill a symmetric zero-diagonal adjacency matrix one row at a
time. The multiset U assigns the remaining degree of vertex i
to later vertices; subtract those incidences from their remaining
degrees. Negative residual degrees are rejected. This generates
every labeled cubic loopless multigraph once. At completion,
reachability rejects disconnected graphs. For each not-yet-seen
matrix, count one class and mark every vertex permutation
from its orbit. The matrix remains fixed while that orbit is
processed, so subsequent isomorphic matrices are skipped.
The vertex count starts at two and advances by two.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 3 terms in 10 s; the official b-file contains 20 terms.
- The bar includes the connected loopless cubic multigraphs on 2, 4 and 6 vertices. Degree enumeration and isomorphism orbits have high cost at larger orders.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 597 | first entry |
| 2026-11-06 | Python 3 | 596 | simplify equivalent expressions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000421), CC BY-SA 4.0.
