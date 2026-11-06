from math import*
from functools import*
@cache
def G(d,i,b):
 if d<2:return 1
 p=P[i];t=p;v=p*G((d+1)//2,i+1,1)
 for e in range(2,min(b,d-1)+1):
  t*=p
  if t>=v:break
  v=min(v,t*G((d+e)//(e+1),i+1,e))
 return v
P=[];p=5;n=1
print(0)
while 1:
 n+=1
 while len(P)<(2*n).bit_length():
  if all(p%q for q in range(2,isqrt(p)+1)):P+=[p]
  p+=4
 print(G(2*n-1,0,2*n-2))
