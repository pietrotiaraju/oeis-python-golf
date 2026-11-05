import math
a=n=1
while[print(a)]:a=sum(2**~-math.gcd(j,n)+2**(n-j%2>>1)for j in range(n))//n;n+=1
