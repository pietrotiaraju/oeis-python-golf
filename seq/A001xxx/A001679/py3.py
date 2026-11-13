A=[m:=-1,m,1];print(1)
for x in A:print(-(sum(map(int.__mul__,A,A[::-1]))+m%2*A[m//2-1])//2);A+=sum(d*A[1-d]*sum(A[d:1:d]+A[d-1:1:d])for d in range(m,0))//m-A[-1],;m-=1
