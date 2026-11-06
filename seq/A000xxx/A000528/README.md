# A000528

> Number of types of Latin squares of order n. Equivalently, number of nonisomorphic 1-factorizations of K_{n,n}.
> — [OEIS A000528](https://oeis.org/A000528)

Offset 1: 1, 1, 1, 2, 2, 17, 324, 842227, 57810418543, 104452188344901572, …

### Python 3 — 449 bytes

```python
from itertools import*
n=1
while 1:
 Q=list(permutations(range(n)));C=set()
 def f(L):
  r=len(L)
  if r==n:
   H=[]
   for T in(L,list(zip(*L))):
    for q in Q:
     for a in T:
      z=[a[q[i]]for i in range(n)]
      H+=[tuple(sorted(tuple(z.index(b[q[i]])for i in range(n))for b in T))]
   C.add(min(H))
  else:
   for p in Q:
    if p[0]==r and all(p[j]not in[b[j]for b in L]for j in range(n)):f(L+[p])
 f([tuple(range(n))]);print(len(C));n+=1
```

**How it works**

- Enumerate reduced Latin squares: the first row and first column are
  0,…,n−1. Every Latin-square type has at least one such representative.
  A new row is accepted only if it repeats no symbol in any column.
- For each square, try every column order and every possible first row.
  That row determines the unique symbol permutation making it 0,…,n−1.
  Sorting the normalized rows removes the remaining row order.
- Also perform this normalization on the transpose. Taking the minimum
  over these choices gives one canonical representative under row,
  column and symbol permutations together with transposition, the OEIS
  definition of type. The set `C` retains one representative per type.

**Notes**

- This is an exact exhaustive orbit enumeration; it includes the transpose
  operation and does not identify additional permutations of roles.
- The search becomes expensive rapidly. The bar covers orders 1 through 5;
  no finite list of Latin-square counts is embedded.
- The reference file contains 11 published OEIS terms; the verification
  bar is 5 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 449 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000528), CC BY-SA 4.0.
