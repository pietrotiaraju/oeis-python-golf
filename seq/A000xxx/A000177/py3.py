f=lambda n,k=6,i=1:(n==1)+sum(f(n-j*j,k-1,j)for j in range(i,n*k))
n=1
while[print(f(n))]:n+=1
