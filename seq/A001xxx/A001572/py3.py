A=[s:=1,n:=1];Q=[-1]
while[print(s)]:Q=[s:=-sum(map(int.__mul__,A[1:],Q))]+Q;n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
