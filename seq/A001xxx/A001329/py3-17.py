from math import*
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or prod(sum(l*(lcm(i,j)%l<1)for l in L)**gcd(i,j)for i in L for j in L)
n=0
while[print(f(n))]:n+=1
