from math import*
n=0
while n:=n+1:
 if all(isqrt(t:=n*n-k*k)**2!=t for k in range(1,n)):print(n*n)
