A=[1,n:=1]
while 1:
 if n>3:
  B=1<<((n+2)**2);M=B**(n+1);S=sum(A[j]*B**j for j in range(1,n+1))
  print(4*(13+14*S+3*S*S)*(1+S)*pow(1-S,-7,M)//B**(n-4)%B)
 n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
