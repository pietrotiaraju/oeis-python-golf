from math import*
from functools import*
f=cache(lambda n,R:sum(perm(n-1,p)*f(n+~p,(*sorted(R+((4,p+1),)),))for p in range(n))if n else R==()or g(R[1:],*R[0]))
def g(R,e,a,N=[]):
 if R:(s,b),*R=R;G=gcd(a,b);return sum(comb(G,m)*g(R,e-m*b//G,a,N+[(s-m*a//G,b)])for m in range(min(e*G//b,s*G//a)+1))
 return(a|~e)%2*comb(a//2,e//2)*f(0,(*sorted(N),))
n=1
while[print(f(n,())//perm(n))]:n+=1
