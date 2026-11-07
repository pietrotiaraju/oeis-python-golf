n=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^i%N for y in m];r=len({*m})>>n;k+=r
  for x in m:
   while-1<x:m[x],x=~r,m[x];r<<=x<0
  t+=r**3>>3*(1in map(m.count,m))
 print(t//k);n+=1
