import math,functools as F
g=F.cache(lambda m,j,p=0:sum(math.comb(m,q)*g(m-q,j-1,q)<<p*q for q in range(m+1)if j)or m<1)
a=[]
while[print(x:=g(n:=len(a),n)-sum(math.comb(n,j)*a[j]*g(n-j,n-1)for j in range(n)))]:a+=x,
