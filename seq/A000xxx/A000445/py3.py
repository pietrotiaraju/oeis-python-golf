from math import*
from functools import*
def J(a,n):
 t=1;a%=n
 while a:
  while a%2<1:a//=2;t*=1-2*(n%8 in(3,5))
  a,n=n,a;t*=1-2*(a%4==n%4==3);a%=n
 return t*(n==1)
P=cache(lambda n:next((p for p in range(2,isqrt(n)+1)if n%p<1),n))
def Q(n):
 O=[]
 for r in range(2,n+1):
  if n%(r*(1+3*(r%4!=1))):continue
  x=r;u=()
  while x>1:
   p=P(x);x//=p
   if x%p<1:break
   u+=p,
  else:O+=(r,u),
 return O
def S(d,C):
 def f(F):
  x=len(F);p=P(x)
  return max([x-1 if c==F[-1]==0 else f(V)for c in(range(d)if p==x else[(F[p]+F[x//p])%d])if x!=2 or d%(c or d)<1 for V in[F+[c]]if all(max(u)!=x or sum(V[p]for p in u)%2==e for u,e in C)]+[0])
 return f([0,0])
def V(n):
 L=Q(n);b=0
 for d,E in{(d:=gcd(a-1,n),tuple((u,(1-J(r,a))//2)for r,u in L)if d%2<1 else())for a in range(1,n)if gcd(a,n)<2}:b=max(b,S(d,E))
 for p in range(2,n+1):
  if n%p<1 and P(p)==p:
   R={x**n%p for x in range(1,p)}
   b=max(b,min([x for x in R if x+1 in R]or[0]))
 return b
n=2
while 1:print(V(n));n+=1
