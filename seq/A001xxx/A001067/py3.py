import math
r=[t:=1];p=1
while[r<[t%2]or print(-(x:=t*(p:=p*-4))//math.gcd(x,(p^-p*p)*p))]:r=[t:=t+x for x in[-t]+r[::-1]]
