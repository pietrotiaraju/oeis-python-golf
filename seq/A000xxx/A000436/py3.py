import math
a=[n:=1]
while[print(abs(a[-1]))]:a+=2-sum(math.comb(2*n,2*k)*9**k*a[-k]for k in range(n+1)),;n+=1