n=1
while 1:
 A=[t:=1]+[0]*~-n
 for p in range(2,n):
  if t%p:
   for j in range(n-1,p-1,-1):A[j]+=A[j-p]
  t*=p*p
 print(*A[n//2:],sep='\n');n*=2
