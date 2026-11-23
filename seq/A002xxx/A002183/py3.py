from heapq import*
H=heappush;h=[(1,1,2,1,9e999)];r=0
while 1:
 x,s,p,e,f=heappop(h);t=s*e
 if t>r:r=t;print(t)
 e<f!=H(h,(x*p,s,p,e+1,f));q=p+1
 while pow(x,q,q)<1:q+=1
 e>1!=H(h,(x*q,t,q,2,e))
