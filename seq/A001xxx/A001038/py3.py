n=1
while 1:
 N=2**n;Q=[]
 for i in range(N**n):
  for _ in[m:=[0]]*n:m+=[y^i%N for y in m];i>>=n
  c=[0]*N*2;z=1
  for x in m:
   k=0
   while~x:m[x],x=-1,m[x];k-=1
   if k:c[k]+=1;z*=~k*c[k]
  Q+=[(z,*c)]*-max(m)
 print(sum(Q.count(K)**2*K[0]for K in{*Q})//len(Q)**2);n+=1
