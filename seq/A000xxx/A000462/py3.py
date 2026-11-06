n=1
while 1:
 r=n;s='';k=1
 while k*(k+1)//2<=n:k+=1
 while k>1:
  k-=1;d,r=divmod(r,k*(k+1)//2);s+=str(d)
 print(s);n+=1
