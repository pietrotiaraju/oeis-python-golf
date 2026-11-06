n=1
while 1:
 N=1<<n;t=k=0
 for z in range(1<<(n*n)):
  P=[0]
  for j in range(n):P+=[x^(z%N)for x in P];z>>=n
  if len(set(P))==N:
   c=0;k+=1
   for x in range(N):
    if P[x]>=0:
     c+=1
     while P[x]>=0:y=P[x];P[x]=-1;x=y
   t+=1<<c
 print(t//k);n+=1
