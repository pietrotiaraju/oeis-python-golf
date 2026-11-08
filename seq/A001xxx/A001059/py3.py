import math
a=[n:=1]
while[print(a[-1])]:a+=sum(math.comb(n,k)**2*a[k]*a[~k]for k in range(n)),;n+=1
