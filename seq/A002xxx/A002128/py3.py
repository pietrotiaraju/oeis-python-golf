f=lambda n,k=3,j=1:sum(e//i*f(n-e,k-1,i+1)for i in range(j,n+1)for e in range(i,n+1,i))if k else n<1
n=6
while[print(f(n))]:n+=1
