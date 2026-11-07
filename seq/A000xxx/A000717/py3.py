from math import*
f=lambda r,*L:r<1or sum(f(r+k,*L,k)*(1+X**-k)**(~k//2)*(1+-~k%2*X**(-k//2))*prod((1+X**lcm(k,l))**gcd(k,l)for l in L)for k in range(-r,0))//r
n=1
while 1:X=1<<n*n;print(f(n)//X**(n*n-n>>2)%X);n+=1
