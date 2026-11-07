from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
A=lambda n:sum(1+2*isqrt(n-a-b)for a in Q for b in Q if a+b<=n)
X=lambda n:H*H*A(n)-s(n*isqrt(12*n*H**4))
p=n=0;Q=[0];H=4**6
print(1)
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while abs(d:=abs(X(n))-abs(X(p)))<n*H:H*=2
 0<d==print(A(p:=n))
