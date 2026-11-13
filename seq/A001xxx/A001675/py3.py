import math
t=l=1;q=z=4;n=0
while 4*z**n//t**n<(a:=4*(z+q)**n//t**n)or[print(-~math.isqrt(a)//2),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
