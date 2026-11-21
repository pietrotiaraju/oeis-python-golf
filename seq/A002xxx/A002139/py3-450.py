from math import*
N=0
while 1:
 N+=2;L=1
 for x in range(N):
  y=x;k=1
  while(y:=(2*y-(2*y<N))%N)-x:k+=1
  L=lcm(L,k)
 print(L)
