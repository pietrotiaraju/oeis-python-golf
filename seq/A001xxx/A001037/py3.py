g=lambda n:2**n-sum(g(d)for d in range(1,n)if n%d<1)
n=0
while[print(g(n)//(n or 1))]:n+=1
