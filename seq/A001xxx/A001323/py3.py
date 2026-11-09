from math import*
f=lambda r,*L:r and sum(f(r+~v//3,*L,~v)for v in range(3*r))//r//3or 3**(sum(prod((t//(g:=gcd(t,v//3))*v%3<1)*3**g for v in L)for t in range(N))//N)
N=3;n=1
while[print(f(n))]:n+=1;N*=n
