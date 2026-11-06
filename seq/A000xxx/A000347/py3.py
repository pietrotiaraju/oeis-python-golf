import math
f=lambda b,m,k=4:k<1or sum(f(b+~c,x,k-1)for x in range(1,m+1)if(c:=math.isqrt(M*M*x-1))<b)
n=M=4
while(a:=f(M*n,n*n))<f(M*n+4,n*n)or[print(a),n:=n+1]:M*=2