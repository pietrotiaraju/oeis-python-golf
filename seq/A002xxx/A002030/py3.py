from math import*
A=lambda n,k=5:k<2or sum(comb(n,r)*A(r,k-1)<<r*(n-r)for r in range(n+1))
L=[]
while[print(a:=A(n:=len(L))-sum(comb(n,k)*k*L[k]//n*A(n-k)for k in range(n)))]:L+=a,
