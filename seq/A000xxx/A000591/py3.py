from math import*
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def f(p):return prod(sum(d for d in p if j%d<1)for j in p)
n=0
while 1:
 H=factorial(n);T=0
 for p in P(n):
  q=p+(1,1);r=tuple(j//gcd(j,2)for j in q for _ in range(gcd(j,2)))
  T+=H//prod(j**p.count(j)*factorial(p.count(j))for j in set(p))*(f(q)**2+f(r))
 print(T//(2*H));n+=1
