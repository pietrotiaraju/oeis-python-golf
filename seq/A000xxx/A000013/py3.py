import math
n=1;k=0
while[print(sum(1<<(g:=math.gcd(j,n))-n//g%2for j in range(n))//n)]:n+=k;k=1
