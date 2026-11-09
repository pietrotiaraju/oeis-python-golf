n=1
while 1:
 t=k=0
 for i in range(1<<n*n):
  for _ in[m:=[0]]*n:m+=[y^i%2**n for y in m];i>>=n
  r=len({*m})>>n;k+=r;u=v=w=r
  for x in m:
   L=-1
   while~x:m[x],x=-1,m[x];L+=1
   if~L:u*=8;v<<=1+2*(L%3<1);w<<=3-L%2
  t+=u+8*v+6*w
 print(t//k//48);n+=1
