from math import*
from functools import*
@cache
def D(d):return{d}|{z for x in range(2,isqrt(d)+1)if d%x<1 for z in(x,d//x)}
@cache
def F(d,i,b):return 1 if d<2 else min([P[i]**(j-1)*v for j in D(d)if j<=b and(v:=F(d//j,i+1,j))]or[0])
P=[];p=5;n=1
print(0)
while 1:
 n+=1
 while len(P)<(2*n).bit_length():
  if all(p%q for q in range(2,isqrt(p)+1)):P+=[p]
  p+=4
 print(min(F(2*n-1,0,2*n-1),F(2*n,0,2*n)))
