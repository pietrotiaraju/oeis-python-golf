from math import*
A=[3,-1,-1,1,1,0,0,2,14];C=[0]*9;q=r=0;k=3
while 1:A+=sumprod(A[-4:],(k,2-k,~k,k+4)),;q=sumprod(A[-10:],(3,-15,24,-24,27,9,-36,32,-14,2))-q;t=r=q-r;C=[t:=t+c for c in C];print(t//3);k+=1
