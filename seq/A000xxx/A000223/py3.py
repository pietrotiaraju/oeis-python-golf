from math import*
s=lambda t,d=3:t and t+s(t*~-d//4//d,d+2)
X=lambda n:G*sum(a+b+c<=n for a in Q for b in Q for c in Q)-s(n*isqrt(12*n*G*G))
p=n=0;Q=[0];G=8**8
while Q:=Q+[n:=n+1,n]*(isqrt(n)**2==n):
 while min(abs(d:=abs(x:=X(n))-abs(X(p))),(y:=x+G//2)%G)<n*G**.5:G*=2
 if d>0:print(y//G);p=n
