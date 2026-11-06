# A000470

> Number of permutations of an n-sequence discordant with three given permutations (see reference) in n-5 places.
> — [OEIS A000470](https://oeis.org/A000470)

Offset 5: 13, 72, 595, 4096, 39078, 379760, 4181826, 49916448, 647070333, 9035216428, …

### Python 3 — 240 bytes

```python
from math import*
n=5
while 1:
 B=(4*n)**n;z=B*B;w=z*z;a=b=c=0;d=1
 for v in([0,-2*z,-2*z*(1+B),3*w]+[0]*n)[:n]:a,b,c,d=b,c,d,(1+3*B)*d-2*z*c-z*(1+B)*b+w*a+v
 print(sum((-1)**(k-5)*comb(k,5)*perm(n-k)*(d//B**k%B)for k in range(5,n+1)));n+=1
```

**How it works**

Let R_n(t)=sum(sigma_(n,k)*t^k,k>=0) be the rook polynomial
from Margolius's bivariate generating function in the OEIS.
Multiplying its denominator gives
R_n=(1+3t)R_(n-1)-2t²R_(n-2)-(t²+t³)R_(n-3)+t⁴R_(n-4),
with numerator corrections -2t² at n=2, -2t²(1+t) at n=3,
and 3t⁴ at n=4; R_0=1 and negative-index terms are zero.
The four scalar states evaluate these polynomials at t=B.
For n>=3, a rook coefficient is at most C(n,k)²*k!
<=4^n*n!<(4n)^n=B, so base-B digits recover every
coefficient without carries. Finally extract y^5 from
sum(sigma_(n,k)*(n-k)!*(y-1)^k,k=0..n): its coefficient
is (-1)^(k-5)*C(k,5). The factorial is `perm(n-k)`.
All arithmetic is exact; polynomial constants come from the
generating function rather than from sequence terms.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 19 terms in 60 s; the official b-file contains 19 terms.


## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 240 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000470), CC BY-SA 4.0.
