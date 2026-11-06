from math import*
A=[[1,0,0,0],[0,0,0,0]];n=1
while 1:
 n+=1;A+=[[0]+[(n-1)*(A[-1][k]+A[-2][k-1])for k in range(1,4)]]
 if n>5:print(A[-1][3])
