from math import*
n=0
while[print(sum((comb(n,k)*comb(2*k,k))**2*comb(2*k,n-k)for k in range(n+1)))]:n+=1
