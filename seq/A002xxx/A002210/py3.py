B=8;p=b=0
while B:=2*B:
 for U in 1<<B,-1<<B:
  z=l=-1;k=1
  while k<B:l+=(t:=U//(k<<k));z+=2*t//k;k+=1
  Z=[z+l*l//U]
  for m in range(5,B,2):Z+=sum(map(int.__mul__,Z,Z[::-1]))*2//(m*U),
  S=sum((z-U)//n//j for n,z in enumerate(Z,1)for j in range(n,2*n));E=U
  while k:E=U+E*S//(k*(l+B+4));k-=1
  a,b=b,str(E*10**B//U)
 while a[:p+1]==b[:p+1]:print(a[p]);p+=1
