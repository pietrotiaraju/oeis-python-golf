# A000465

> Number of bipartite partitions of n white objects and 4 black ones.
> — [OEIS A000465](https://oeis.org/A000465)

Offset 0: 5, 12, 29, 57, 109, 189, 323, 522, 831, 1279, …

### Python 3 — 284 bytes

```python
from math import*
a=[1];n=0;F=[];Q=[[0]*k for k in range(1,5)]
while 1:
 t=a[-1]
 for L in Q:t+=L.pop(0);L+=[t]
 F+=[t];print(sum(x*y for x,y in zip([5,2,0,-3,-5,-1,0,3,1,-1],F[::-1])))
 n+=1;a+=[sum((k%2*2-1)*a[-k*(3*k-1)//2]for k in range(-isqrt(n),isqrt(n)+1)if 0<k*(3*k-1)//2<=n)]
```

**How it works**

Let P(x) be the ordinary partition series. Euler's q-binomial
identity gives product((1-y^j*x^i)^(-1),i>=0)
=sum(y^(j*m)/D_m(x),m>=0), where D_m=product(1-x^k,k=1..m).
Sum over partitions of the fixed number 4 of black objects.
This gives P(x)*N(x)/D_4(x), where N has coefficient list
[5, 2, 0, -3, -5, -1, 0, 3, 1, -1].
The program generates P with Euler's pentagonal recurrence.
A queue of length k applies 1/(1-x^k) via z(n)=input(n)+z(n-k).
After those filters, take the short convolution with N.
This derives the count for every n, including the black-only case n=0.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 5001 terms in 60 s; the official b-file contains 5001 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 284 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000465), CC BY-SA 4.0.
