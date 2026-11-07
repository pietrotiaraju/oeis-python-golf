from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(D:=lambda j,m=2*lcm(*L):1<<sum(R:=[prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m)])//m+(0in R))(1)**2+6*D(2)+8*D(3)//D(1)
n=1
while[print(f(n)//24)]:n+=1
