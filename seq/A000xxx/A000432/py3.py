A=[1,n:=1]
while 1:B=64**n;T=sum(A[k]*B**k for k in range(n));print(4*T*-~T*pow(2-T,-5,B**n)*B//B**n%B);n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,