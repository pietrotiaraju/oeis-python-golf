f=lambda n:n*n-sum(f(d)for d in range(1,n)if n%d<1)
n=1
while[print(n*f(n))]:n+=1
