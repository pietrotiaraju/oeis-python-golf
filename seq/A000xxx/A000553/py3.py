from math import*
f=lambda n,p,h:sum(comb(n,k)*p**k*f(n-k,k,h-1)for k in range(1,n+1))if h else n<1
n=5
while[print(n*f(n-1,1,4))]:n+=1
