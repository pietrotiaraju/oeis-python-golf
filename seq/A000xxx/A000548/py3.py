from math import*
n=0
while 1:
 n+=1
 if all(isqrt(n*n-k*k)**2!=n*n-k*k for k in range(1,n)):print(n*n)
