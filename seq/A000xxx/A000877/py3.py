n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n;s=u=r=len({*m})>>n;k+=6*r
  for x in m:
   while~x:m[x],x=-1,m[x];i+=1;r<<=x<0
   s<<=i%2;u<<=i%3%2;i=0
  t+=r*r+3*r*s+2*u*u
 print(t//k);n+=1
