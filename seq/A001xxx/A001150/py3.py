n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n;s=r=len({*m})>>n;k+=8*r
  for x in m:
   while~x:m[x],x=-1,m[x];i^=1;r<<=x<0
   s<<=i;i=0
  t+=r*(r+s+s)
 print(t//k);n+=1
