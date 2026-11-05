import math
x=n=1
while[print(x)]:x=sum(1<<(g:=math.gcd(k,2*n))+(2>>n%2+n%g)for k in range(2*n))//8//n;n+=1
