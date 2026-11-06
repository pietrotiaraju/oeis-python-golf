r=[n:=0,1]
while 1:
 m=-n
 if m>=4:
  B=m**m+1;M=B**(m+1);S=sum(r[j]*B**j for j in range(1,m+1))
  print(S**4*(64-79*S+36*S*S-6*S**3)*pow(1-S,-7,M)//B**m%B)
 n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,
