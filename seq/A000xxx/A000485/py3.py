r=[n:=0,1]
while 1:
 m=-n
 if m>3:
  B=1<<(5*m+8);S=sum(r[k]*B**k for k in range(1,m+1))
  print(S**4*(16-19*S+6*S*S)*pow(1-S,-5,B**(m+1))//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
