import math
f=lambda r,*L:r<1and sum(math.prod(sum(d>>(j<<j%e)%d*d for d in L)**(2-j%e)for j in L)for e in(1,2))or sum(f(r+~k,*L,k+1)for k in range(r))//r
n=0
while[print(f(n,1,1)//2)]:n+=1
