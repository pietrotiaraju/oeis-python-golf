import math
n=1
while 1:
 k=1
 while math.isqrt(n*100**k)%2:k+=1
 print(k);n+=1
