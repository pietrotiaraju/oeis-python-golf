import math
S={2};P=p=1
while p:=p+1:
 if P**p%p:
  S|={s*p for s in S};P*=p;c=0
  for D in S-{4}:
   m=0;d=1;a=b=math.isqrt(D);h,H,k,J,x,y=b,1,1,0,1,0
   while h*h-D*k*k-1:m=d*a-m;d=(D-m*m)//d;a=(b+m)//d;h,H,k,J=a*h+H,h,a*k+J,k
   for i in[0]*(p//2+2):x,y=h*x+D*k*y,h*y+k*x;c+=pow(P,len(bin(y)),y)<1
  print(c)
