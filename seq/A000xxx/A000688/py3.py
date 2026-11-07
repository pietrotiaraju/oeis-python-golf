f=lambda n,m=0:n<2or sum(f(n//d,d)for d in range(2,n+1)if n%d+m%d<1)
n=1
while[print(+f(n))]:n+=1
