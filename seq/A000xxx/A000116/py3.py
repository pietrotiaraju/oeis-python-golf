import math
n=1
while[print(sum(1<<(g:=math.gcd(j,n))-n//g%2for j in range(n))//n)]:n+=2-n%2
