from math import*
n=0
while 1:
 n+=1;r=range(1,isqrt(n)+1)
 if any(isqrt(n-x*x)**2==n-x*x for x in r)and all(isqrt(n-x*x-y*y)**2!=n-x*x-y*y for x in r for y in r if 0<n-x*x-y*y):print(n)
