A=[1,2];B=[1,n:=1]
while[print(A[n]-2*B[n])]:
 n+=1
 for X in A,B:X+=sum(sum(X[-d::-d])*d*X[d]for d in(1,*range(1,n)))//n,
