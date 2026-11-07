from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or 8**(sum(R:=[prod((t//(g:=gcd(t,l))%2*l<1)<<g for l in L)for t in range(2*lcm(*L))])//len(R)+(0in R))
n=1
while[print(f(n)//8)]:n+=1
