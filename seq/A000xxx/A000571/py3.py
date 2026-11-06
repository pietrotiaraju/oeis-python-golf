from math import*
A=[1];B=[0];n=0
while[print(A[-1])]:
 n+=1;B+=sum((-1)**(n+d)*sum(gcd(j,n//d)==1 for j in range(1,n//d+1))*comb(2*d,d)for d in range(1,n+1)if n%d<1)//(2*n),
 A+=sum(B[k]*A[n-k]for k in range(1,n+1))//n,
