from math import*
N=0
while 1:
 N+=2;L=1;s=set()
 for x in range(N):
  k=0
  while{x}-s:s|={x};x=(2*x-(2*x<N))%N;k+=1
  L=lcm(L,k)or L
 print(L)
