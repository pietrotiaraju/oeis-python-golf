import math
f=lambda r,*L:r<1or sum(f(r+k,*L,k)*3**(~k//2+sum(map(math.gcd,L,[k]*n)))for k in range(-r,0))//r
n=1
while[print(+f(n))]:n+=1
