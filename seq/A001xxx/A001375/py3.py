import math
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or 8**sum(math.gcd(a,b)for a in L for b in L)
n=1
while[print(f(n))]:n+=1
