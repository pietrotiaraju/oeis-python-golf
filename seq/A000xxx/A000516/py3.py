from math import*
from functools import*
P=cache(lambda n,m=1:[((j,*p),-z*j*~p.count(j))for j in range(m,n+1)for p,z in P(n-j,j)]if n else[((),1)])
def a(n,k):
 k=min(k,n-k)
 if k<1:return+(k==0)
 T=0;H=factorial(n)**2
 for R,r in P(n):
  for S,s in P(n):
   @cache
   def f(i,j,h,D):
    if i==len(R):return 1
    if j==len(S):return h==0 and f(i+1,0,k,tuple(v for s,v in sorted(zip(S,D))))
    d=gcd(R[i],S[j]);u=S[j]//d;v=R[i]//d
    return sum(comb(d,t)*f(i,j+1,h-t*u,D[1:]+(D[0]-t*v,))for t in range(min(d,h//u,D[0]//v)+1))
   T+=H//r//s*f(0,0,k,(k,)*len(S))
 return T//H
n=0
while 1:n+=1;print(a(n,5))
