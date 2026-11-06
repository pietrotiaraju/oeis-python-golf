# A000448

> Smallest number that is the sum of 2 squares in at least n ways.
> — [OEIS A000448](https://oeis.org/A000448)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 27625, 27625, 71825, 138125, …

### Python 3 — 366 bytes

```python
from math import*
from functools import*
@cache
def G(d,i,b):
 if d<2:return 1
 p=P[i];t=p;v=p*G((d+1)//2,i+1,1)
 for e in range(2,min(b,d-1)+1):
  t*=p
  if t>=v:break
  v=min(v,t*G((d+e)//(e+1),i+1,e))
 return v
P=[];p=5;n=1
print(0)
while 1:
 n+=1
 while len(P)<(2*n).bit_length():
  if all(p%q for q in range(2,isqrt(p)+1)):P+=[p]
  p+=4
 print(G(2*n-1,0,2*n-2))
```

**How it works**

As explained on [A000446](../A000446/), a positive minimum
uses only primes 1 mod 4 with decreasing exponents. If their
exponents are e_i, the number of unordered two-square
representations is ceil(product(e_i+1)/2). Thus the threshold
for at least n representations is product(e_i+1)>=2n-1.
G(d,i,b) minimizes the remaining prime-power product, requiring
a divisor-count product at least d, starting at prime P[i],
with the next exponent at most b. After choosing e>=1, the
remaining threshold is ceil(d/(e+1)) and later exponents
are bounded by e. Exponent 1 provides an initial valid
upper bound. Stop increasing e once P[i]^e reaches that
bound, since every remaining factor is at least 1. No
optimal candidate is discarded. Memoization makes the exact
search practical. The first term is separately 0=0²+0².

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 10000 terms in 60 s; the official b-file contains 10000 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 366 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000448), CC BY-SA 4.0.
