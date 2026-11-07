from math import*
f=lambda r,*L:r and sum(f(r-abs(k),*L,k)for k in range(-r,r+1)if k)//r>>1or(a:=(C:=lambda j,m=2*lcm(*L):1<<sum(prod((t*j//(g:=gcd(t*j,l))%2*l<1)<<g for l in L)for t in range(m))//m)(1))**3+21*a*C(2)+56*C(3)+42*isqrt(C(2)*C(4))+48*isqrt(C(7)//a)
n=1
while[print(f(n)//168)]:n+=1
