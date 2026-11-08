n=0;f=C=1;c=d=p=q=2
while[print(f+C+q+d+7>>3)]:
 n+=1;f*=n;c,d=d,d+~-n*c
 if~n%2:C*=n;p,q=q,(n-2)*p
