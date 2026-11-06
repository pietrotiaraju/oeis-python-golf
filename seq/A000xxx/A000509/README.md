# A000509

> Size of second largest n-arc in PG(2,q), where q runs through the primes and prime powers >= 7.
> — [OEIS A000509](https://oeis.org/A000509)

Offset 1: 6, 6, 8, 10, 12, 13, 14, 14, 17, 21, …

### Python 3 — 867 bytes

```python
def P(q):
 p=next(p for p in range(2,q+1)if q%p<1);e=0;r=q
 while r%p<1:e+=1;r//=p
 if r>1:return
 R=range(q)
 A=lambda a,b,c=-1:sum((a//p**i-c*(b//p**i))%p*p**i for i in range(e))
 for h in R:
  G=[];t=1
  for _ in R[1:]:
   G+=[t];t=A(t*p,h,t*p//q)
  if t==1 and len(set(G))==q-1:break
 M=lambda a,b:a*b and G[(G.index(a)+G.index(b))%(q-1)]
 return[sum(1<<(x*q+A(M(a,x),b))for x in R)|1<<(q*q+a)for a in R for b in R]+[((1<<q)-1)<<(b*q)|1<<(q*q+q)for b in R]+[((1<<q+1)-1)<<q*q]
q=6
while 1:
 q+=1;L=P(q)
 if L:
  N=len(L);U=(1<<N)-1;B=set();A=(0,1,q,q+1)
  H=[[next(l for l in L if l>>i&l>>j&1)if i!=j else 0 for j in range(N)]for i in range(N)]
  C=0
  for i in A:
   for j in A:C|=H[i][j]
  def f(S,C,V):
   if C==U:B.add(len(S))
   while V:
    b=V&-V;V-=b;j=b.bit_length()-1;D=C
    for i in S:D|=H[i][j]
    f(S+(j,),D,V&~D)
  f(A,C,U&~C);print(sorted(B)[-2])
```

**How it works**

- Enumerate q in increasing order and retain exactly the prime powers
  q=p^e. Encode degree-below-e polynomials over GF(p) by base-p integers.
  `A(a,b,c)` subtracts c times each coefficient of b from that of a;
  its default c=−1 gives field addition without integer carries.
- Try the monic polynomials X^e+h. The update `A(t*p,h,t*p//q)`
  multiplies t by X and reduces its leading coefficient modulo X^e+h.
  Keep the first h for which the successive powers of X contain all q−1
  nonzero encodings and return to 1. Every nonzero residue is then a unit,
  so this quotient is a field. A primitive element of GF(q) has a degree-e
  minimal polynomial, which guarantees that one of these candidates works.
- `G` lists the nonzero powers of that primitive element. Multiplication
  adds their positions modulo q−1; multiplication by zero returns zero.
- Point x·q+y is the affine point (x,y). Build each line y=a·x+b directly,
  adding its point at infinity q²+a. Vertical lines x=b use q consecutive
  affine bits and the common infinity point q²+q. The last mask is the
  line at infinity. These are exactly the q²+q+1 lines of PG(2,q).
- An arc contains no three collinear points. Any four of its points
  form a projective frame, and projective transformations carry any
  frame to the four fixed affine corners used here. Enumerating arcs
  containing that frame therefore retains every possible complete-arc size.
- `C` is the union of secants through all selected pairs. Only points
  outside `C` may be added. The arc is complete exactly when `C`
  covers the whole plane. Ascending candidate indices avoid repeated
  subsets; the second largest distinct complete size is printed.

**Notes**

- Completeness is essential: this implements the complete-arc convention
  of the projective-plane tables cited by OEIS A000509.
- Field construction, incidence, and subset enumeration are exact for
  every prime power. Enumeration grows rapidly; the initial bar checks
  the first two field orders, including a nonprime extension field.
- The reference file contains 12 published OEIS terms; the verification
  bar is 2 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1387 | first entry |
| 2026-11-06 | Python 3 | 867 | primitive-polynomial field arithmetic and direct affine line masks |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000509), CC BY-SA 4.0.
