from math import*
A=lambda n:sum(comb(n,r)<<r*(n-r)for r in range(n+1))
L=[1,2]
while[print(a:=A(n:=len(L))-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
