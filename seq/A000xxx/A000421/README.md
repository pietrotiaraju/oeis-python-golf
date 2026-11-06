# A000421

> Number of isomorphism classes of connected 3-regular (trivalent, cubic) loopless multigraphs of order 2n.
> — [OEIS A000421](https://oeis.org/A000421)

Offset 1: 1, 2, 6, 20, 91, 509, 3608, 31856, 340416, 4269971, …

### Python 3 — 573 bytes

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
   if min(C)<0:continue
   for j in range(i+1,n):A[i][j]=A[j][i]=U.count(j)
   yield from G(i+1,C)
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

- In the code n is the vertex count, twice the OEIS index.
  A cubic graph has total degree 3n=2|E|, so n must be even;
  the outer loop uses 2,4,6,… vertices.
- A is a symmetric adjacency matrix with zero diagonal. Its
  entries count parallel edges. `G(i,D)` has fixed all edges
  incident with earlier vertices; D records the degrees still
  needed from the unprocessed vertices.
- Choose a multiset U of D[i] later vertices to receive vertex
  i's remaining incidences. Repetitions in U permit parallel
  edges; using only vertices greater than i excludes loops and
  avoids choosing an edge twice.
- Copy D to C and subtract those incidences from C[j]. A negative
  remaining degree rejects the choice. Set A[i][j]=A[j][i]
  to U's multiplicity of j and recurse. Processed entries of C
  stay nonnegative and are never read again for degree choices,
  so `min(C)<0` tests the whole vector and no entry needs clearing.
  These choices generate every labeled loopless cubic multigraph once.
- At a completed matrix, grow the set V of vertices reachable
  from 0. Repeating at most n times reaches every vertex in its
  component; yield the matrix only if `len(V)==n`.
- The yielded tuple lists the strict upper triangle in fixed
  column order. If it is absent from S, count a new isomorphism
  class and insert every vertex relabeling into S.
- The generator stays suspended during those relabelings, so its
  current A still represents the yielded tuple. Resuming G only
  afterwards allows later isomorphic matrices to be skipped.

**Notes**

- Parallel edges are not individually labeled. Their multiplicity
  is one matrix entry, so permuting copies of an edge creates no
  extra graph. Vertex relabeling is handled by the complete orbit.
- On two vertices there is just the graph with three parallel
  edges. On four vertices the two classes are K₄ and a 4-cycle
  with a pair of opposite edges doubled.
- Connectivity, degree constraints and orbit equality are all exact
  finite checks. Dividing the labeled count by n! would fail
  because automorphism group sizes vary; explicitly marking the
  orbits avoids that assumption.
- Degree assignments, n! vertex permutations for each new class,
  and the stored orbit tuples all grow rapidly. This exhaustive
  method is mathematically valid for every order, with runtime
  and memory limiting the orders reached in practice.
- The b-file has 20 terms (indices 1 through 20). The bar is the
  first 3 terms in 10 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 597 | first entry |
| 2026-11-06 | Python 3 | 596 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 573 | keep processed degree entries and check the whole degree vector |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000421), CC BY-SA 4.0.
