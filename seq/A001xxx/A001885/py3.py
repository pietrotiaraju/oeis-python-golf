from functools import*
n=1
while f:=cache(lambda r,m,j:r<1or j*f(r-1,m>>1,j+1)+~-x*sum(f(r-1,m+b>>1,j)for b in(1,2,4)[:r+1]if~m&b)):n+=1;x=n**n;print(f(n,1,1)//x**2%x)
