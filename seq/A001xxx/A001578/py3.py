import math
a=b=L=d=1
while[print(d)]:
 a,b=b,a+b;Q=a//math.gcd(a,L**3);L*=a;d=2
 while Q%d:d=[Q,d+1][d*d<Q]
