import math
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or math.prod(sum(j*(i%j<1)for j in L)for i in L)
n=0
while[print(f(n))]:n+=1
