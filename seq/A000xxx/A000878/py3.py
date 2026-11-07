n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n;s=u=v=w=r=len({*m})>>n;k+=168*r
  for x in m:
   while~x:m[x],x=-1,m[x];i+=1;r<<=x<0
   s<<=i%2;u<<=i%3%2;v<<=i%4==1;w<<=i%7==1;i=0
  t+=r*(r*r+21*s*(r+2*v)+56*u*u)+48*w**3
 print(t//k);n+=1
