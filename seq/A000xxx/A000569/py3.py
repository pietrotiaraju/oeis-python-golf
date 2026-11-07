f=lambda s,m=1,p=():s<1and all(sum(p[:r])<=r*r-r+sum(min(x,r)for x in p[r:])for r in range(n))or sum(f(s-j,j,(j,)+p)for j in range(m,s+1))
n=2
while[print(f(n))]:n+=2
