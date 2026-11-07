import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<k*k-3*sum(k*d*e//math.lcm(k,d,e)for d in L for e in(*L,k))for k in range(-r,0))//r
n=1
while[print(f(n))]:n+=1
