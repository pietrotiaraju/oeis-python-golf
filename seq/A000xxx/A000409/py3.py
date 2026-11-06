from math import*
s=[0,2,-3,1];n=2
while[print(-sum(s[k+1]*comb(2**k-1,n)for k in range(n)))]:
 n+=1;s=[0]+[s[k-1]-n*s[k]for k in range(1,n+1)]+[1]
