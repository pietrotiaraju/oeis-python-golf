# A000451

> Smallest number that is the sum of 3 squares in at least n ways.
> — [OEIS A000451](https://oeis.org/A000451)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

### Python 3 — 168 bytes

```python
n=k=0;s=[];d={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 while t<=d.get(n,0):print(n);t+=1
 n+=1
```

**How it works**

Count unordered triples of nonnegative squares exactly as in
[A000437](../A000437/). Scan candidate integers in increasing order.
If the current integer has c representations, it is the smallest
qualifying value for every not-yet-output threshold t<=c; print it
for each such threshold before continuing.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 200 terms in 60 s; the official b-file contains 200 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 168 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000451), CC BY-SA 4.0.
