from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
X=lambda n:G*sum(2*isqrt(n-a-b)+1for a in Q for b in Q if a+b<=n)-s(n*isqrt(12*n*G*G))
p=n=0;Q=[0];G=8**8
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*G**.5:G*=2
 0<d==print(p:=n)
