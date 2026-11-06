from math import*
n=5
while 1:print(sum((-1)**j*comb(n+1,j)*(5-j)**n for j in range(5)));n+=1
