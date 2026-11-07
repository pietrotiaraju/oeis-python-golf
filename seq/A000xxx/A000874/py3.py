from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(C:=lambda j,m=2*lcm(*L):1<<sum(prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m))//m)(1)**2+3*C(2)+2*C(3)//C(1)
n=1
while[print(f(n)//6)]:n+=1
