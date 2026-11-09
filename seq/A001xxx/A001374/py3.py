import math,functools
f=functools.cache(lambda r,*L:r<1or sum(f(r-k,*sorted((*L,k)))<<2*k+4*sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r)
n=1
while[print(+f(n))]:n+=1
