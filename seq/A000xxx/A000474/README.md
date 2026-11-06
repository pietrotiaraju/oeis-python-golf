# A000474

> Number of nonisomorphic 1-factorizations of complete graph K_{2n}.
> — [OEIS A000474](https://oeis.org/A000474)

Offset 1: 1, 1, 1, 6, 396, 526915620, 1132835421602062347, …

### Python 3 — 512 bytes

```python
from itertools import*
F=frozenset
E=lambda a,b:1<<((c:=max(a,b))*~-c//2+a+b-c)
M=lambda V:(e|E(a,b)for a,*W in[V]for b in W for e in M([x for x in W if x!=b]))if V else[0]
H=lambda E:((x,*t)for x in L if x&E&-E and x&E==x for t in H(E^x))if E else[()]
n=2
while 1:
 R=range(n);L=[*M(R)];S=set();c=0
 for t in H((1<<n*~-n//2)-1):
  if F(t)in S:continue
  c+=1
  for p in permutations(R):
   B=[E(p[i],p[j])for j in R for i in range(j)]
   S.add(F(sum(b*(x>>k&1)for k,b in enumerate(B))for x in t))
 print(c);n+=2
```

**How it works**

- First enumerate the labeled factorizations of K_n by the
  least-uncovered-edge construction of [A000438](../A000438/).
  The code uses n=2,4,6,… vertices, twice the OEIS index.
- M generates each perfect matching as an edge bit mask. H(E)
  chooses a matching containing `E&-E`, removes it and yields
  the remaining factor tuple. The empty graph yields the empty
  tuple, completing one exact-cover path.
- The forced least-edge order counts each unordered factorization
  once. For isomorphism testing, `frozenset(t)` explicitly removes
  factor order from its representation.
- If this frozenset is not already in S, increment the class count.
  `E(a,b)` supplies the triangular edge bit shared by matching generation
  and relabeling. Its larger endpoint c gives index c(c−1)/2+a+b−c.
- For every vertex permutation p, B lists the image bits of all edges,
  generated in triangular order by j and then i<j.
- `sum(b*(x>>k&1)for k,b in enumerate(B))` makes the relabeled mask
  of matching x. The multiplier selects precisely its occupied edge bits.
  Distinct edges have distinct image bits, so the sum is their bitwise
  union. Store the frozenset of those masks in S.
- Thus the whole vertex-permutation orbit is marked before the
  next factorization is considered. Every isomorphism class is
  encountered and counted exactly once.

- In the exact-cover generator, `x&E&-E` tests whether matching
  x contains the least remaining edge. This is the same pivot-edge
  choice without storing a separate p at each recursion level.

- M is a lazy generator expression when vertices remain, with
  `[0]` as its empty-matching iterable. The single unpacking
  `for a,*W in[V]` keeps the least-vertex choice and remaining
  order of the recursive generator, without an explicit function body.

- H is likewise lazy: for nonempty E it yields `(x,*t)` for each
  valid first matching and recursively generated remainder. At E=0,
  `[()]` supplies the single empty factorization.

**Notes**

- Vertex relabeling preserves adjacency and factor membership.
  Factor names are already discarded; the orbit calculation
  handles the remaining vertex isomorphisms.
- One cannot generally divide the labeled factorization count by
  n!: different factorizations have different stabilizers. For K₈,
  the 6240 labeled objects of [A000438](../A000438/) fall
  into six classes, the first nontrivial output of this page.
- Exact integer masks and exhaustive permutations make the procedure
  independent of graph-isomorphism heuristics or numerical tests.
- The work includes both exact-cover enumeration and n! relabelings
  for each new orbit representative. S stores every marked image,
  so memory as well as runtime grows sharply beyond small orders.
- The b-file has 7 terms (indices 1 through 7). The bar is the
  first 4 terms in 20 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 639 | first entry |
| 2026-11-06 | Python 3 | 631 | simplify equivalent expressions |
| 2026-11-06 | Python 3 | 621 | inline the least-edge test and shorten the matching base case |
| 2026-11-06 | Python 3 | 579 | use lazy lambdas for matchings and exact covers |
| 2026-11-06 | Python 3 | 550 | read each matching bit directly while relabeling |
| 2026-11-06 | Python 3 | 512 | share the edge encoder and generate relabeling indices directly |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000474), CC BY-SA 4.0.
