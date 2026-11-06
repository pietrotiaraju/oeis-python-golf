# A000585

> Number of equivalence classes of Boolean functions of n variables under GL(n,2).
> — [OEIS A000585](https://oeis.org/A000585)

Offset 1: 4, 8, 20, 92, 2744, 950998216, 2076795963681989019155896, 21651217007530946175606768762255421159692845640522169779616, …

### Python 3 — 258 bytes

```python
n=1
while 1:
 N=1<<n;t=k=0
 for z in range(1<<(n*n)):
  P=[0]
  for j in range(n):P+=[x^(z%N)for x in P];z>>=n
  if len(set(P))==N:
   c=0;k+=1
   for x in range(N):
    if P[x]>=0:
     c+=1
     while P[x]>=0:y=P[x];P[x]=-1;x=y
   t+=1<<c
 print(t//k);n+=1
```

**How it works**

- Enumerate n×n binary matrices by their n columns. `P` lists the
  images of every vector, built by adjoining XOR translates for each
  new basis vector.
- A matrix is invertible exactly when these 2^n images are distinct.
  These are precisely GL(n,2), with no affine translations.
- An invertible matrix permutes the input vectors. A Boolean function
  is fixed exactly when it is constant on each permutation cycle, so
  a map with c cycles fixes 2^c functions.
- The destructive cycle walk counts c; averaging its fixed-function
  count over all invertible matrices is Burnside's lemma.

**Notes**

- Both constant functions and the zero input vector are included.
  Output complementation and affine translations are excluded.
- Exhaustive matrix enumeration costs 2^(n²); the bar is n=1,…,4.
  The method remains exact at every order.
- The reference file contains 8 terms from the OEIS b-file; the verification
  bar is 4 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 258 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000585), CC BY-SA 4.0.
