n=0
while 1:
 r=n;s='';k=1
 while k**3<=n:k+=1
 while k>1:
  k-=1;d,r=divmod(r,k**3);s+=str(d)
 print(s or 0);n+=1
