A=[1,n:=1]
while 1:
 B=1<<(5*n+3);S=sum(A[k]*B**k for k in range(1,n))
 print(4*(2+S)*(1+S)*pow(1-S,-5,B**n)//B**(n-1)%B)
 n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
