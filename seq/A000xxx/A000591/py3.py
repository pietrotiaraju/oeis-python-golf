from math import*
P=lambda n,m=1:[()]if n<1else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
f=lambda p:prod(sum(d for d in p if j%d<1)for j in p)
n=0
while 1:
 H=factorial(n);T=0
 for p in P(n):
  q=p+(1,1);r=[j//gcd(j,2)for j in q for _ in range(gcd(j,2))]
  T+=H//prod(j*(i+1-p.index(j))for i,j in enumerate(p))*(f(q)**2+f(r))
 print(T//(2*H));n+=1
