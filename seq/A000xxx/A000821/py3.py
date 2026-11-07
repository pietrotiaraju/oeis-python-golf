n=r=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^~i%N for y in m];t+=r**3;r=len({*m})>>n;k+=r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
