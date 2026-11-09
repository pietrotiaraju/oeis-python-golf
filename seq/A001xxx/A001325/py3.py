from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(m:=2*lcm(*L))and 3**(sum(3**sum((g:=gcd(t,l))*(t//g%2*l<1)for l in L)for t in range(m))//m)
n=1
while[print(f(n))]:n+=1
