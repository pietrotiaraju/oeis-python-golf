from math import*
A=[[1]*3];n=0
while 1:
 n+=1;B=[1]+[sum(comb(n-1,k-1)*k*A[k-1][j-1]*A[n-k][j]for k in range(1,n+1))for j in range(1,3)];A+=B,
 if n>=3:print((n+1)*(B[-1]-B[-2]))
