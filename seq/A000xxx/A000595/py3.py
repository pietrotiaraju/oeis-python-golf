from math import*
from functools import*
@cache
def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1,1)for p in P(n-j,j)]
n=0
while 1:
 H=factorial(n);print(sum((H//prod(j**p.count(j)*factorial(p.count(j))for j in set(p)))*2**sum(gcd(i,j)for i in p for j in p)for p in P(n))//H);n+=1
