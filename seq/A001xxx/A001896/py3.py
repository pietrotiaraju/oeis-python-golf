import math
r=[t:=1];p=1
print(1)
while[r<[t%2]or print(-(x:=len(r)*t*((p:=p*4)-2))//math.gcd(x,p*p-p))]:r=[t:=x-t for x in[t]+r[::-1]]