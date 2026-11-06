# A000510

> Maximal number of points in PG(2,q) with at most 3 on a line (next term is 21 or 22).
> — [OEIS A000510](https://oeis.org/A000510)

Offset 2: 7, 9, 9, 11, 15, 15, 17, …

### Python 3 — 1314 bytes

```python
from math import*
def plane(q):
 p=next((d for d in range(2,isqrt(q)+1)if q%d==0),q);e=0;r=q
 while r%p==0:e+=1;r//=p
 if r>1:return
 def digits(a,m=e):return[a//p**i%p for i in range(m)]
 def rem(a,b):
  a=a*1;d=len(b)-1
  for j in range(len(a)-1,d-1,-1):
   c=a[j]
   for i in range(d+1):a[j-d+i]=(a[j-d+i]-c*b[i])%p
  return a[:d]
 h=next(digits(z)+[1]for z in range(q)if all(any(rem(digits(z)+[1],digits(w,d)+[1]))for d in range(1,e//2+1)for w in range(p**d)))
 A=[[sum((x+y)%p*p**i for i,(x,y)in enumerate(zip(digits(a),digits(b))))for b in range(q)]for a in range(q)]
 M=[]
 for a in range(q):
  row=[]
  for b in range(q):
   c=[0]*(2*e-1)
   for i,x in enumerate(digits(a)):
    for j,y in enumerate(digits(b)):c[i+j]=(c[i+j]+x*y)%p
   row+=[sum(x*p**i for i,x in enumerate(rem(c,h)))]
  M+=[row]
 X=[(1,a,b)for a in range(q)for b in range(q)]+[(0,1,a)for a in range(q)]+[(0,0,1)]
 return[sum(1<<j for j,x in enumerate(X)if A[A[M[l[0]][x[0]]][M[l[1]][x[1]]]][M[l[2]][x[2]]]==0)for l in X]
q=1
while 1:
 q+=1;L=plane(q)
 if L:
  N=len(L);U=(1<<N)-1;B=0;H=[[l for l in L if l>>j&1]for j in range(N)]
  def f(S,V):
   global B
   n=S.bit_count();B=max(B,n)
   while n+V.bit_count()>B:
    b=V&-V;V-=b;T=S|b;D=0
    for l in H[b.bit_length()-1]:
     if(T&l).bit_count()==3:D|=l
    f(T,V&~D)
  f(0,U);print(B)
```

**How it works**

- Construct each Desarguesian plane PG(2,q), in increasing prime-power
  order q≥2, by exact finite-field arithmetic. Points and lines use
  normalized homogeneous coordinates, with incidence decided by the
  vanishing dot product.
- Search all point subsets, keeping at most three chosen points on each
  line. After inserting a point, every incident line that now has three
  selected points excludes all its other points from future candidates.
- `B` is the largest valid subset found. A branch is stopped only when
  its selected size plus all remaining candidates cannot exceed `B`.
  Ascending candidate indices cover every subset once, so this bound
  cannot discard a better solution.
- The initial plane is the Fano plane q=2: every line has three points,
  so all seven points are admissible and the first output is 7.

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

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000510), CC BY-SA 4.0.
