from math import*
n=1
while 1:print(3*comb(n,2)*sum(comb(n,k+2)*comb(n,k)*comb(n-2,k)for k in range(n-1))+3*n*n*sum(comb(n,k+1)*comb(n-1,k+1)*comb(n-1,k)for k in range(n-1)));n+=1
