k=s=1;m=0
while 1:
 k+=4;s+=-~s*-~s<=k;h=0;S={(a,b)for b in range(1,-~s*all(k%d for d in range(2,-~s)),2)for a in range(s-b+2&-2,s-~b,2)if(k-b*b)%(2*a)<1}
 while S:
  a,b=S.pop();h+=1
  while(a:=(k-b*b)//a,b:=s-(s+b)%a)in S:S-={(a,b)}
 if h>m:print(k);m=h
