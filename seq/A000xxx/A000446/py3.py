from math import*
from functools import*
D=cache(lambda d:{d}|{z for x in range(2,isqrt(d)+1)if d%x<1 for z in(x,d//x)})
F=cache(lambda d,i,b: 1 if d<2 else min([P[i]**~-j*v for j in D(d)if j<=b and(v:=F(d//j,i+1,j))]or[0]))
P=[];p=t=n=1
print(0)
while n:=n+1:
 while len(P)<(2*n).bit_length():
  t*=p*p;p+=1;P+=[p]*(t%p>0<p%4==1)
 print(min(F(k:=n+n,0,k),F(k-1,0,k-1)))
