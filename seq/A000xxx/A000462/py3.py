n=1
while 1:
 r=n;s='';t=k=1
 while t<=n:k+=1;t+=k
 while k>1:
  t-=k;k-=1;d,r=divmod(r,t);s+=str(d)
 print(s);n+=1
