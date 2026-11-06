# A000491

> Number of bipartite partitions of n white objects and 5 black ones.
> — [OEIS A000491](https://oeis.org/A000491)

Offset 0: 7, 19, 47, 97, 189, 339, 589, 975, 1576, 2472, …

### Python 3 — 296 bytes

```python
from math import*
a=[1];n=0;F=[];Q=[[0]*k for k in range(1,6)]
while 1:
 t=a[-1]
 for L in Q:t+=L.pop(0);L+=[t]
 F+=[t];print(sum(x*y for x,y in zip([7,5,2,-2,-7,-9,-6,1,4,6,3,1,-3,-2,1],F[::-1])))
 n+=1;a+=[sum((k%2*2-1)*a[-k*(3*k-1)//2]for k in range(-isqrt(n),isqrt(n)+1)if 0<k*(3*k-1)//2<=n)]
```

**How it works**

Let P(x) be the ordinary partition series. Euler's q-binomial
identity gives product((1-y^j*x^i)^(-1),i>=0)
=sum(y^(j*m)/D_m(x),m>=0), where D_m=product(1-x^k,k=1..m).
Sum over partitions of the fixed number 5 of black objects.
This gives P(x)*N(x)/D_5(x), where N has coefficient list
[7, 5, 2, -2, -7, -9, -6, 1, 4, 6, 3, 1, -3, -2, 1].
The program generates P with Euler's pentagonal recurrence.
A queue of length k applies 1/(1-x^k) via z(n)=input(n)+z(n-k).
After those filters, take the short convolution with N.
This derives the count for every n, including the black-only case n=0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1001 terms in 60 s; the official b-file contains 1001 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 296 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000491), CC BY-SA 4.0.
