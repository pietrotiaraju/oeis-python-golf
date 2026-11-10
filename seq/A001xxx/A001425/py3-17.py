from math import*
f=lambda r,*L:r and sum(f(k,*L,r-k)for k in range(r))//r or isqrt(prod(sum(l>>(lcm(i,j)>>(j<0))%l*l for l in L)**gcd(i,j)for i in L for j in L+(-2,)))
n=0
while[print(f(n))]:n+=1
