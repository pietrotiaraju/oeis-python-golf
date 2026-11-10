from math import*
f=lambda r,W,*L:sum(f(r-j,W*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)%M//j//-~L.count(j),*L,j)for j in range(1,min(L+(r,))+1))if r else W
n=1
while 1:B=n*n;M=1<<B*-~n;F=factorial(n);print(f(n,F<<4*B)//F>>B*n);n+=1
