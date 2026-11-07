n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=1
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  if max(m)<0:Q=lambda j:2**sum(m.count(v)%j<1for v in{*m});a=r<<Q(2)//r;k+=48;t+=a*(a*a+6*(r*Q(2)<<Q(4)//r)+8*Q(3)**2)
 print(t//k);n+=1
