from math import gcd,isqrt
from functools import cache
def J(a,n):
 t=1;a%=n
 while a:
  while a%2==0:
   a//=2
   if n%8 in (3,5):t=-t
  a,n=n,a
  if a%4==n%4==3:t=-t
  a%=n
 return t if n==1 else 0
@cache
def factor(n):
 return next((p for p in range(2,isqrt(n)+1)if n%p==0),n)
def quadratic_relations(n):
 out=[]
 for r in range(2,n+1):
  D=r if r%4==1 else 4*r
  if n%D:continue
  x=r;ps=[]
  while x>1:
   p=factor(x);x//=p
   if x%p==0:break
   ps.append(p)
  else:out.append((r,ps))
 return out
def search(d,conditions):
 def rec(F):
  x=len(F);p=factor(x)
  cs=range(d)if p==x else [(F[p]+F[x//p])%d]
  if x==2:cs=[c for c in cs if c==0 or d%c==0]
  best=0
  for c in cs:
   V=F+[c]
   if any(max(ps)==x and sum(V[p]for p in ps)%2!=e for ps,e in conditions):continue
   v=x-1 if c==F[-1]==0 else rec(V)
   best=max(best,v)
  return best
 return rec([0,0])
def value(n):
 rel=quadratic_relations(n);types=set();answer=0
 for a in range(1,n):
  if gcd(a,n)>1:continue
  d=gcd(a-1,n)
  cond=tuple((tuple(ps),(1-J(r,a))//2)for r,ps in rel)if d%2==0 else ()
  if (d,cond)in types:continue
  types.add((d,cond));answer=max(answer,search(d,cond))
 for p in range(2,n+1):
  if n%p==0 and factor(p)==p:
   R={pow(x,n,p)for x in range(1,p)}
   answer=max(answer,min((x for x in R if x+1 in R),default=0))
 return answer
n=2
while 1:print(value(n));n+=1
