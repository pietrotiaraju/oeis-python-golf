n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=1
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  if max(m)<0:Q=lambda j:2**sum(m.count(v)%j<1for v in{*m});k+=168;t+=r*(r*r+21*Q(2)*(r+2*Q(4))+56*Q(3)**2)+48*Q(7)**3
 print(t//k);n+=1
