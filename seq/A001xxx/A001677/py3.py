A=[1,n:=1]
while 1:n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,;print(2*A[n]-(sum(map(int.__mul__,A,A[::-1]))+~n%2*A[n//2])//2)
