n=1
while 1:
 N=1<<n;t=k=0
 for z in range(N**n):
  for _ in[P:=[0]]*n:P+=[x^z%N for x in P];z>>=n
  r=len({*P})>>n;k+=r
  for x in P:
   while~x:P[x],x=-1,P[x];r<<=x<0
  t+=r
 print(t//k);n+=1
