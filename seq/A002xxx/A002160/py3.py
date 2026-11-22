t=l=1;q=z=2;n=0
while 2*z**n//t**n<(a:=2*(z+q)**n//t**n)or[print(a+1>>1),n:=n+1]:l+=2;q*=l//2;z=z*l+q;t*=l
