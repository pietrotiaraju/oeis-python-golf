import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(2*n,2*k)*a[k]*a[n+~k]for k in range(n)),;n+=1
