from math import*
n=m=0
while 1:
 n+=1
 while sum(isqrt(k:=m-x*x)**2==k for x in range(isqrt(m//2)+1))<n:m+=1
 print(m)
