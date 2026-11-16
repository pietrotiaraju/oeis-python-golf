from math import*
a=[n:=1]
while[print(a[-1])]:a+=sum(comb(n-1,k)*(k+(k!=1))*a[~k]for k in range(n)),;n+=1
