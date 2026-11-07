A=[1,n:=1]
while[print(-~A[n]//2)]:n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
