from math import*
f=lambda r,*L:r<1or sum(f(r-k,*L,k)*prod((1+B**lcm(k,d))**gcd(k,d)for d in(*L,*L,k))%B**-~n for k in range(1,r+1))//r
n=0
while 1:B=9**n**2;print(f(2*n)//B**n);n+=1
