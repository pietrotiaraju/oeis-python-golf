f=lambda n,m=2:1+sum(f(n//d,d)for d in range(m,n)if n%d<1>d*d-n)
n=1
while[print(f(n))]:n+=1
