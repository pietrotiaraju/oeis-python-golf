import math
r=[1]
for n in r:r+=n+1,;s=sum(d*(n%d<1)for d in r);sum(math.gcd(j,s)<2for j in range(s))-n or print(n)
