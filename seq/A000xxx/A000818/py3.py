n=1
while 1:
 t=k=r=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^~i%2**n for y in m];i>>=n;t+=r**3;r=len({*m})>>n;k+=r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
