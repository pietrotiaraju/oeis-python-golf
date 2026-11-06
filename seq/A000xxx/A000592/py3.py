from math import*
n=a=0
while 1:
 r=sum(isqrt(n-x*x)**2==n-x*x for x in range(isqrt(n)+1))
 if r:a+=r;print(a)
 n+=1
