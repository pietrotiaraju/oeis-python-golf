import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(n,k)*k**~-k*a[-k]for k in range(1,n+1))//n,;n+=1
