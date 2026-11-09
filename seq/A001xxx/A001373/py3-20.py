import math
f=lambda r,*L:sum(f(k,*L,r-k)for k in range(r))//r if r else math.prod(sum(j*(i%j<1)for j in L)-1for i in L)
n=0
while[print(f(n))]:n+=1
