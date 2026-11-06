from math import*
n=5
while 1:print(n*(sum(comb(n-1,k)*k**(n-1-k)for k in range(n))-(n-1)*(2**(n-2)-1)-1));n+=1
