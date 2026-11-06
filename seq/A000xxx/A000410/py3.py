from itertools import*
n=1
def s(V):
 A=[[(x>>i)&1 for i in R]for x in V]
 for i in R:
  p=next((j for j in range(i,n)if A[j][i]),-1)
  if p<0:return 1
  A[i],A[p]=A[p],A[i]
  for j in range(i+1,n):
   b=A[j][i]
   if b:A[j]=[x*A[i][i]-y*b for x,y in zip(A[j],A[i])]
 return 0
while 1:
 R=range(n);print(sum(s(V)for V in combinations(range(1,1<<n),n)));n+=1
