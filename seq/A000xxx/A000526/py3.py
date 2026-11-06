r=[n:=0,1]
while 1:
 m=-n
 if m>=5:
  B=m**m+1;M=B**(m+1);S=sum(r[j]*B**j for j in range(1,m+1))
  print(S**5*(125-204*S+118*S*S-24*S**3)*pow(1-S,-7,M)//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
