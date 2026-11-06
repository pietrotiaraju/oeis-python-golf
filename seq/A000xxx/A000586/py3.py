from math import*
n=1
while 1:
 A=[1]+[0]*(n-1)
 for p in range(2,n):
  if all(p%d for d in range(2,isqrt(p)+1)):
   for j in range(n-1,p-1,-1):A[j]+=A[j-p]
 print(*A[n//2:],sep='\n');n*=2
