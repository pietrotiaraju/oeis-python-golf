from math import*
from functools import*
J=lambda a,n:1if n<2 else J(n%a,a)*(-1)**(a//2*(n//2))if a%2 else a and J(a//2,n)*(-1)**((n*n-1)//8)
P=cache(lambda n:next((p for p in range(2,isqrt(n)+1)if n%p<1),n))
def S(d,C):
 def f(F):
  x=len(F);p=P(x)
  return max([x-1 if c==F[-1]==0 else f(V)for c in(range(d)if p==x else[(F[p]+F[x//p])%d])if x>2 or d%(c or d)<1 for V in[F+[c]]if all(sum(V[p]for p in u)%2==e for u,e in C if u[-1]==x)]+[0])
 return f([0,0])
def V(n):
 L=[(r,u)for r in range(2,n+1)if n%(r<<2*(r%4!=1))<1 for u in[tuple(p for p in range(2,r+1)if r%p<1 and P(p)==p)]if prod(u)==r]
 T={(d:=gcd(a-1,n),tuple((u,(1-J(r,a))//2)for r,u in L)if d%2<1 else())for a in range(1,n)if gcd(a,n)<2}
 return max([S(d,E)for d,E in T]+[min(R&{x-1for x in R}or{0})for p in range(2,n+1)if n%p<1 and P(p)==p for R in[{x**n%p for x in range(1,p)}]])
n=2
while 1:print(V(n));n+=1
