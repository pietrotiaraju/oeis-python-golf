from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(t:=max(1,*L))and any((t*(l>0)+l)//gcd(t,l)%2for l in L)<<sum(prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(2*lcm(*L)))//lcm(*L)//4
n=1
while[print(f(n))]:n+=1
