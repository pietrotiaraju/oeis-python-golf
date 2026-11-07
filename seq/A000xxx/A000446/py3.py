F=lambda d,i:d<2or min(P[i]**~-k*F(d//k,i+1)for k in range(2,d+1)if d%k<1)
c=0;P=[];p=t=1
while 1:
 while 2**len(P)<=c:t*=p*p;p+=1;P+=[p]*(t%p>0<p%4<2)
 print(c and min(F(c+1,0),F(c+2,0)));c+=2
