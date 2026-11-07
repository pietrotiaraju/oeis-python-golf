import math
m=1
while B:=4**m:M=B**m;T=0;print((sum((T-(T:=B*math.prod(pow(1-B**j,-(T//B**j%B),M)for j in range(m))%M))**2for _ in[0]*m)*B//M%B+m%2*T//B**(m//2)%B)//2);m+=1
