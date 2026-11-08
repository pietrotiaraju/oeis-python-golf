P=p=1
while 1:
 P*=p*p;p+=1
 if P%p:
  r=range(2,p//2+1);M=[[i*pow(j,-1,p)//p for j in r]for i in r];q=1
  while M:(a,*R),*M=sorted(M,key=lambda r:r[0]==0);M=[[(x*a-y*b)//q for x,y in zip(s,R)]for b,*s in M];q=a
  print(abs(q))
