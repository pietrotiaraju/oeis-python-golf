import math,functools as F
g=F.cache(lambda m,p=0,j=7:sum(math.comb(m,q)*g(m-q,q,j-1)<<p*q for q in range(m+1)if j)or m<1)
n=0
while[print(g(n))]:n+=1
