from math import*
f=lambda r,W,*L:r and sum(f(r-j,W*(1<<B*j|1)**(~-j//2)*(~j%2<<B*j//2|1)*prod((1<<B*lcm(j,l)|1)**gcd(j,l)for l in L)%M//j//-~L.count(j),*L,j)for j in range(1,min(L+(r,))+1))or W
n=1
while 1:
 m=n+2;B=n*n;M=1<<B*-~m;L=[0];P=[1]
 for i in range(1,n+1):P+=f(i,F:=factorial(i))//F,;L+=i*P[i]-sum(L[j]*P[~j]for j in range(i))%M,
 print(((L[n]>>B*m)-~n%2*(L[n//2]>>B*m//2)%(1<<B))//n);n+=1
