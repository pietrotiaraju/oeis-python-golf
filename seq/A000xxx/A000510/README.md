# A000510

> Maximal number of points in PG(2,q) with at most 3 on a line (next term is 21 or 22).
> — [OEIS A000510](https://oeis.org/A000510)

Offset 2: 7, 9, 9, 11, 15, 15, 17, …

### Python 3 — 781 bytes

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
q=1
while 1:
 q+=1;L=P(q)
 if L:
  N=len(L);U=(1<<N)-1;B=0;H=[[l for l in L if l>>j&1]for j in range(N)]
  def f(S,V):
   global B
   n=S.bit_count();B=max(B,n)
   while n+V.bit_count()>B:
    b=V&-V;V-=b;T=S|b
    f(T,V&~sum(l^b for l in H[b.bit_length()-1]if(T&l).bit_count()==3))
  f(0,U);print(B)
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
- Search all point subsets, keeping at most three chosen points on each
  line. After inserting a point, every incident line that now has three
  selected points excludes all its other points from future candidates.
- `B` is the largest valid subset found. A branch is stopped only when
  its selected size plus all remaining candidates cannot exceed `B`.
  Ascending candidate indices cover every subset once, so this bound
  cannot discard a better solution.
- The initial plane is the Fano plane q=2: every line has three points,
  so all seven points are admissible and the first output is 7.

Distinct lines through the inserted point `b` meet only at that point.
Thus `l^b` removes their sole shared bit and leaves disjoint masks, whose
sum equals their bitwise union. `V` already excludes `b`, so this excludes
exactly the same future candidates as the union of the full lines.

**Notes**

- Both field construction and maximization are exhaustive algorithms,
  with no stored maxima or unproved formula for later planes.
- Prime-power enumeration follows the q convention of the OEIS entry;
  the sequence index is not used as a composite field order.
- Running time is exponential in the number of points. The bar checks
  the first three planes, including the extension field GF(4).
- The reference file contains 7 published OEIS terms; the verification
  bar is 3 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1314 | first entry |
| 2026-11-06 | Python 3 | 794 | primitive-polynomial field arithmetic and direct affine line masks |
| 2026-11-06 | Python 3 | 781 | sum disjoint incident-line masks after removing the shared point |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000510), CC BY-SA 4.0.
