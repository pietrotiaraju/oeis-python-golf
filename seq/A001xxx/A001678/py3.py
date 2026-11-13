A=[0,0,1];m=-1
for x in A:print(x);A+=sum(d*A[1-d]*sum(A[d::d]+A[d-1::d])for d in range(m,0))//m-A[-1],;m-=1
