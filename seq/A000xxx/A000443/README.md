# A000443

> Numbers that are the sum of 2 squares in exactly 3 ways.
> — [OEIS A000443](https://oeis.org/A000443)

Offset 1: 325, 425, 625, 650, 725, 845, 850, 925, 1025, 1250, …

### Python 3 — 118 bytes

```python
n=k=0;s=[];d={}
while 1:
 if n==k*k:
  s+=[n];k+=1
  for x in s:d[n+x]=d.get(n+x,0)+1
 if d.get(n,0)==3:print(n)
 n+=1
```

**How it works**

Whenever a new square n=k² appears, pair it with every square
0<=x<=n and increment the counter for n+x. Each unordered pair
of nonnegative squares is counted exactly once, when its largest
square appears. At candidate n, all representations of n have
already been counted. Print precisely when that counter is three.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000443), CC BY-SA 4.0.
