from itertools import*
def G(i,D):
 if i==n:
  V={0}
  for _ in R:V|={j for i in V for j in R if A[i][j]}
  if len(V)==n:yield tuple(A[i][j]for j in R for i in range(j))
 else:
  for U in combinations_with_replacement(range(i+1,n),D[i]):
   C=D*1
   for j in U:C[j]-=1
   if min(C)<0:continue
   for j in range(i+1,n):A[i][j]=A[j][i]=U.count(j)
   yield from G(i+1,C)
n=2
while 1:
 R=range(n);A=[[0]*n for _ in R];S=set();c=0
 for t in G(0,[3]*n):
  if t in S:continue
  c+=1
  for p in permutations(R):S.add(tuple(A[p[i]][p[j]]for j in R for i in range(j)))
 print(c);n+=2
