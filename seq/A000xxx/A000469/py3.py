from math import*
n=1
while 1:
 r=range(2,isqrt(n)+1)
 if all(n%(k*k)for k in r)and(n==1 or any(n%k<1 for k in r)):print(n)
 n+=1
