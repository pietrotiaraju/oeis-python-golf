from functools import*
f=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)-sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r+1]if~m&b))
n=0
while[print(+f(n,1,1))]:n+=1
