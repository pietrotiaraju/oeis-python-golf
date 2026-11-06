from math import gcd,isqrt
from functools import cache
def J(a,n):
 t=1;a%=n
 while a:
  while a%2<1:
   a//=2
   if n%8 in(3,5):t=-t
  a,n=n,a
  if a%4==n%4==3:t=-t
  a%=n
 return t*(n==1)
@cache
def P(n):
 return next((p for p in range(2,isqrt(n)+1)if n%p<1),n)
def Q(n):
 O=[]
 for r in range(2,n+1):
  D=r if r%4==1 else 4*r
  if n%D:continue
  x=r;u=[]
  while x>1:
   p=P(x);x//=p
   if x%p<1:break
   u.append(p)
  else:O.append((r,u))
 return O
def S(d,C):
 def f(F):
  x=len(F);p=P(x)
  U=range(d)if p==x else [(F[p]+F[x//p])%d]
  if x==2:U=[c for c in U if c==0 or d%c==0]
  B=0
  for c in U:
   V=F+[c]
   if any(max(u)==x and sum(V[p]for p in u)%2!=e for u,e in C):continue
   v=x-1 if c==F[-1]==0 else f(V)
   B=max(B,v)
  return B
 return f([0,0])
def V(n):
 L=Q(n);T=set();b=0
 for a in range(1,n):
  if gcd(a,n)>1:continue
  d=gcd(a-1,n)
  E=tuple((tuple(u),(1-J(r,a))//2)for r,u in L)if d%2==0 else ()
  if (d,E)in T:continue
  T.add((d,E));b=max(b,S(d,E))
 for p in range(2,n+1):
  if n%p<1 and P(p)==p:
   R={pow(x,n,p)for x in range(1,p)}
   b=max(b,min([x for x in R if x+1 in R]or[0]))
 return b
n=2
while 1:print(V(n));n+=1
