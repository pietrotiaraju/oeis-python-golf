n=0
while 1:
 c=p=1;s=k=0
 while 1:
  k+=1;c*=k;s*=k;p*=n
  if k%2:s+=p*(-1)**(k//2)
  else:c+=p*(-1)**(k//2)
  e=2*p*n;t=k+1
  if k>2*n and c*c*t*t>e*e and len(q:={(s*t+i*e)//(c*t+j*e)for i in(-1,1)for j in(-1,1)})<2:print(*q);break
 n+=1
