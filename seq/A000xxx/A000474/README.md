# A000474

> Number of nonisomorphic 1-factorizations of complete graph K_{2n}.
> — [OEIS A000474](https://oeis.org/A000474)

Offset 1: 1, 1, 1, 6, 396, 526915620, 1132835421602062347, …

### Python 3 — 631 bytes

```python
from itertools import*
def M(V):
 if not V:yield 0
 else:
  a,*W=V
  for b in W:
   for e in M([x for x in W if x!=b]):yield e|1<<(b*(b-1)//2+a)
def H(E):
 if not E:yield()
 else:
  p=E&-E
  for x in L:
   if x&p and x&E==x:
    for t in H(E^x):yield(x,*t)
n=2
while 1:
 L=list(M(range(n)));A=[(i,j)for j in range(n)for i in range(j)];S=set();c=0
 for t in H((1<<len(A))-1):
  if frozenset(t)in S:continue
  c+=1;Q=[[k for k in range(len(A))if x>>k&1]for x in t]
  for p in permutations(range(n)):
   B=[1<<((b:=max(p[i],p[j]))*(b-1)//2+min(p[i],p[j]))for i,j in A]
   S.add(frozenset(sum(B[k]for k in q)for q in Q))
 print(c);n+=2
```

**How it works**

Enumerate every unordered 1-factorization by the exact-cover
construction of [A000438](../A000438/), then quotient by all
vertex permutations. Matchings are edge masks; a factorization
is a frozenset of matching masks, so factor order is immaterial.
Whenever a factorization has not yet been seen, count one new
isomorphism class and add every vertex relabeling to S.
Its entire orbit is then skipped by subsequent enumerated
factorizations. This is an exhaustive finite procedure for
each n, with no precomputed sequence values.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 4 terms in 20 s; the official b-file contains 7 terms.
- Both exact-cover enumeration and vertex-permutation orbits grow quickly. The bar includes the first nontrivial six classes on eight vertices.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 639 | first entry |
| 2026-11-06 | Python 3 | 631 | simplify equivalent expressions |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000474), CC BY-SA 4.0.
