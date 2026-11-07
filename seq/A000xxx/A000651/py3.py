from math import*
a=[n:=0]
while[print(a[n])]:a+=(105>>n%6*2&3)+a[n]+sum((-1)**k*comb(n-k,k+1)*a[~k]for k in range(n)),;n+=1
