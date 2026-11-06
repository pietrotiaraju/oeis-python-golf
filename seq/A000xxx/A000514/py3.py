from math import*
n=6
while 1:print(sum((-1)**j*comb(n+1,j)*(6-j)**n for j in range(6)));n+=1
