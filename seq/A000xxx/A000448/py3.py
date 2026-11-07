from functools import*
@cache
def G(c,i):
 p=t=P[i];v=p**c;k=2
 while t<v:v=min(v,t*G(c//k,i+1));t*=p;k+=1
 return v
c=0;P=[];p=t=1
while 1:
 while 2**len(P)<=c:t*=p*p;p+=1;P+=[p]*(t%p>0<p%4<2)
 print(c and G(c,0));c+=2
