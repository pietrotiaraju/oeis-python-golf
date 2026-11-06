# A000437

> Smallest nonnegative number that is the sum of 3 squares in exactly n ways.
> — [OEIS A000437](https://oeis.org/A000437)

Offset 1: 0, 9, 41, 81, 146, 194, 306, 369, 425, 594, …

### Python 3 — 197 bytes

```python
n=k=0;s=[];d={};a={};t=1
while 1:
 if n==k*k:
  s+=[n];k+=1
  for i,x in enumerate(s):
   for y in s[:i+1]:d[n+x+y]=d.get(n+x+y,0)+1
 a.setdefault(d.get(n,0),n)
 while t in a:print(a[t]);t+=1
 n+=1
```

**How it works**

On encountering a new largest square n, enumerate pairs of
nonnegative squares y<=x<=n. Each triple is counted once, when
its largest square appears. At each candidate integer n its
representation counter is therefore complete. `setdefault` records
the first integer having each number of representations. The next
requested count t is printed only after it has been found; this
permits the nonmonotone output values in the definition.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 43 terms in 60 s; the official b-file contains 43 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 197 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000437), CC BY-SA 4.0.
