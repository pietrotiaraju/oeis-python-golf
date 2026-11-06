from math import*
from functools import*
@cache
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def a(n,k):
 if k<0 or k>n:return 0
 k=min(k,n-k)
 if k==0:return 1
 T=0;H=factorial(n)
 for R in P(n):
  w=H//prod(j**R.count(j)*factorial(R.count(j))for j in set(R))
  for S in P(n):
   @cache
   def f(i,D):
    if i==len(R):return int(not any(D))
    r=R[i]
    def g(j,k,E):
     if j==len(S):return f(i+1,tuple(v for s,v in sorted(zip(S,E))))if k==0 else 0
     s=S[j];d=gcd(r,s);u=s//d;v=r//d
     return sum(comb(d,t)*g(j+1,k-t*u,E+(D[j]-t*v,))for t in range(min(d,k//u,D[j]//v)+1))
    return g(0,k,())
   T+=w*(H//prod(j**S.count(j)*factorial(S.count(j))for j in set(S)))*f(0,(k,)*len(S))
 return T//(H*H)
n=0
while 1:n+=1;print(a(n,4))
