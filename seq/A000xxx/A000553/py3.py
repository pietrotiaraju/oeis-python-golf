f=lambda n,p,h:n|h<1or sum(((2**n+1)**n>>n*k)%2**n*p**k*f(n-k,k,h-1)for k in range(1,n*h+1))
n=5
while[print(n*f(n-1,1,4))]:n+=1
