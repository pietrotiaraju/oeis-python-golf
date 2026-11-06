import math
f=lambda r,*L:r<1or sum(f(r-k,*L,k)<<k//2-~sum(map(math.gcd,L,[k]*n))for k in range(1,r+1))//r
n=1
while[print(f(n)>>1)]:n+=1
