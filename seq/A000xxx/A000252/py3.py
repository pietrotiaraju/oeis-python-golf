f=lambda n,k:n**k-sum(f(d,k)for d in range(1,n)if n%d<1)
n=1
while[print(n*f(n,1)*f(n,2))]:n+=1
