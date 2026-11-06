# A000446

> Smallest number that is the sum of 2 squares (allowing zeros) in exactly n ways.
> — [OEIS A000446](https://oeis.org/A000446)

Offset 1: 0, 25, 325, 1105, 4225, 5525, 203125, 27625, 71825, 138125, …

### Python 3 — 410 bytes

```python
from math import*
from functools import*
@cache
def D(d):return{d}|{z for x in range(2,isqrt(d)+1)if d%x<1 for z in(x,d//x)}
@cache
def F(d,i,b):return 1 if d<2 else min((P[i]**(j-1)*v for j in D(d)if j<=b and(v:=F(d//j,i+1,j))),default=0)
P=[];p=5;n=1
print(0)
while 1:
 n+=1
 while len(P)<(2*n).bit_length():
  if all(p%q for q in range(2,isqrt(p)+1)):P+=[p]
  p+=4
 print(min(F(2*n-1,0,2*n-1),F(2*n,0,2*n)))
```

**How it works**

For positive N, the number of unordered representations as two
nonnegative squares is ceil(D/2), where D=product(e+1) over
prime factors p=1 mod 4, provided all primes 3 mod 4 have even
exponent. Removing factors 2 and squares of primes 3 mod 4
preserves that count and decreases N, so a minimum uses only
primes 1 mod 4. Assign exponents in decreasing order to those
primes in increasing order. F(d,i,b) enumerates multiplicative
partitions of d via the factors j=e+1 in decreasing order;
it returns the minimum product starting with prime P[i].
Infeasible branches return 0 and are filtered out. Trial division
generates enough eligible primes, since at most log2(d) factors
are needed. The special first value is 0=0²+0².
Exactly n representations require D=2n-1 or D=2n; take the smaller minimum.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 1458 terms in 60 s; the official b-file contains 1458 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 410 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000446), CC BY-SA 4.0.
