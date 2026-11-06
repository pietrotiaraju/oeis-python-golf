from math import*
n=0
while 1:
 n+=1;r=range(1,isqrt(n)+1)
 if any(isqrt(t:=n-x*x)**2==t for x in r)and all(isqrt(t)**2!=t for x in r for y in r if(t:=n-x*x-y*y)>0):print(n)
