from math import*
A=lambda n:sum(comb(n,j)<<j*(n-j)for j in range(n+1))
L=[0]
while[print(a:=A(n:=len(L))//2-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
