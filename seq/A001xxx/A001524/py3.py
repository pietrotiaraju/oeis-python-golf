from functools import*
G=cache(lambda i,n:(n%i<1)+sum(d*G(i+1,n-i*d)for d in range(1,n//i)))
n=0
while[print(G(1,n))]:n+=1
