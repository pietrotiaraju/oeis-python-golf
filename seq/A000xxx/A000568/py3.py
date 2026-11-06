from math import*
from functools import*
P=cache(lambda n,m=1:[()]if n<1else[(j,)+p for j in range(m,n+1,2)for p in P(n-j,j)])
n=0
while 1:
 H=factorial(n);print(sum(H//prod(j*(i+1-p.index(j))for i,j in enumerate(p))*2**((sum(gcd(i,j)for i in p for j in p)-len(p))//2)for p in P(n))//H);n+=1
