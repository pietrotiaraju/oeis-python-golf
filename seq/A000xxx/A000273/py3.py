import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)<<~k+2*sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r
n=0
while[print(+f(n))]:n+=1
