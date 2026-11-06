from math import*
n=4
while 1:print(sum((-1)**k*perm(n-k)*comb(k,4)*comb(2*n-k,k)for k in range(4,n+1)));n+=1
