import math
f=lambda b,m:sum(1+f(b+~c,x)for x in range(1,m+1)if(c:=math.isqrt(M*M*x-1))<b)
n=M=1
while(a:=f(M*n,n*n))<f(M*n+n,n*n)or[print(a),n:=n+1]:M*=2