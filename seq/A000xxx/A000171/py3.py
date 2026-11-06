import math
f=lambda r,*L:r<1or sum(n%4%3*f(r+k,*L,k)<<2*~k+4*sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
n=2
while[print(+f(n+1>>2))]:n+=1
