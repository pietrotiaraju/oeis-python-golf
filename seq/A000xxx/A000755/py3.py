f=lambda P,r=0:r==n or sum(f(P+[(r,a),(r,b)],r+1)for a in range(n)for b in range(a)if len({(c,(y-c<<n)//(r-x))for c in(a,b)for x,y in P})==4*r)
n=1
while[print(f([]))]:n+=1
