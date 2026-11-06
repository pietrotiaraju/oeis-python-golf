# A000417

> Euler transform of A000389.
> — [OEIS A000417](https://oeis.org/A000417)

Offset 1: 1, 7, 28, 105, 357, 1232, 4067, 13301, 42357, 132845, …

### Python 3 — 161 bytes

```python
from math import*
a=[1];b=[0]
while 1:
 n=len(a);b+=[sum(k*comb(k+4,5)for k in range(1,n+1)if n%k<1)]
 a+=[sum(b[k]*a[n-k]for k in range(1,n+1))//n];print(a[-1])
```

**How it works**

The generating function is product((1-x^k)^(-C(k+4,5)),k>=1).
Its logarithmic derivative has coefficient
b(n)=sum(d*C(d+4,5),d dividing n).
Thus n*a(n)=sum(b(k)*a(n-k),k=1..n), with a(0)=1.
The program stores both coefficient lists and prints from n=1.
This Euler product is the specified Euler transform; it is not
the actual high-dimensional partition sequence.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1000 terms in 60 s; the official b-file contains 1000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 161 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000417), CC BY-SA 4.0.
