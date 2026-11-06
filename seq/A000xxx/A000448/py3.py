from functools import*
@cache
def G(d,i,b):
 if d<2:return 1
 t=p=P[i];v=p*G(-~d//2,i+1,1)
 for e in range(2,min(b+1,d)):
  t*=p
  if t>=v:break
  v=min(v,t*G((d+e)//-~e,i+1,e))
 return v
P=[];p=t=n=1
print(0)
while n:=n+1:
 while len(P)<(2*n).bit_length():
  t*=p*p;p+=1;P+=[p]*(t%p>0<p%4==1)
 print(G(d:=2*n-1,0,d-1))
