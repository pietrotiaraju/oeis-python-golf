from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and sum(L)+n and 1<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(m))//m
n=0
while[print(f(n))]:n+=1
