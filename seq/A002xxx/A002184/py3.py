import math
n=P=1
while 1:
 t=2**n-1;c=t//math.gcd(t,P);P*=t;p=n+1
 while c%p:p=[c,p+n][p*p<c]
 print(p);n+=2
