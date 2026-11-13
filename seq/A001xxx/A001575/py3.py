A=[1,3];B=[1,2];C=[1,n:=1]
while[print(A[n]-3*B[n]+3*C[n])]:
 n+=1
 for X in A,B,C:X+=sum(sum(X[-d::-d])*d*X[d]for d in(1,*range(1,n)))//n,
