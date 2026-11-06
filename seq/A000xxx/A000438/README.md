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

M enumerates perfect matchings by pairing the least remaining
vertex with each possible partner. An edge {a,b}, a<b, has bit
b*(b-1)/2+a. F(E) counts partitions of the remaining edge set
into perfect matchings. Choose its least edge p; the matching
containing p is uniquely determined within each factorization,
so summing over compatible matchings counts each unordered
factorization exactly once. Memoize the remaining edge masks.
The complete graph on n vertices has all C(n,2) low bits set;
advance n by two after each count.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 4 terms in 10 s; the official b-file contains 7 terms.
- This exact-cover enumeration has exponential cost. The bar includes K_2 through K_8; later complete graphs require substantially more resources.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 311 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000438), CC BY-SA 4.0.
