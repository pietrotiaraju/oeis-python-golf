# A000427

> Number of 7-dimensional partitions of n.
> — [OEIS A000427](https://oeis.org/A000427)

Offset 1: 1, 8, 36, 148, 554, 2024, 7134, 24796, 84625, 285784, …

### Python 3 — 266 bytes

```python
d=8
S={frozenset()}
while S:
 T=set()
 for s in S:
  for v in {(0,)*d}|{tuple(x+(j==i)for j,x in enumerate(u))for u in s for i in range(d)}:
   if v not in s and all(tuple(x-(j==i)for j,x in enumerate(v))in s for i in range(d)if v[i]):T.add(s|{v})
 S=T;print(len(S))
```

**How it works**

A 7-dimensional partition is a finite order ideal of N^8
with the coordinatewise order. Start with the empty ideal.
An element can be added exactly when all its immediate lower
neighbors already belong to the ideal. Every nonempty ideal
has a maximal element whose removal gives an earlier ideal,
so this construction reaches every ideal of the next size.
Frozensets remove duplicate constructions without identifying
coordinate permutations. Print the number of ideals after
each size increase; this is the actual partition count rather
than the different MacMahon Euler-product prediction.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 7 terms in 10 s; the official b-file contains 20 terms.
- This exhaustive construction grows quickly in time and memory. The bar is the first seven terms; later sizes remain mathematically exact but require more resources.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 266 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000427), CC BY-SA 4.0.
