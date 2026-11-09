from math import*
f=lambda r,*L:r<1or sum(f(r-j,*L,j)*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)for j in range(1,r+1))%M//r
h=lambda a,b:(L[a]>>B*b&X-1)-sum(h(a//k,b//k)for k in range(2,a+1)if a%k+b%k<1)
n=2
while 1:
 m=n*~-n+3>>2;B=n*n;X=1<<B;M=X<<B*m;L=[0];P=[1]
 for i in range(1,n+1):P+=f(i),;L+=i*P[i]-sum(L[j]*P[~j]for j in range(i))%M,
 print(h(n,m)//n);n+=1
