import math
r=[n:=1]
while[print(r[-1])]:r+=sum(2**~-(c:=math.gcd(j,n))+2**(n-j%2>>1)-n*r[j]*(c==j)for j in range(n))//n,;n+=1
