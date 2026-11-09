P=[];N=m=r=1;D=2
while 1:
 m+=1;r+=r*r<=m
 if all(m%d for d in range(2,r)):P+=m,;N*=m;D*=m-1
 while N>D:print(m);N//=P[0];D//=P.pop(0)-1
