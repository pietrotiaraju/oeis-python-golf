from math import*
A=[-1,1,1,0,0];F=[0]*7;k=1
while 1:A+=sumprod(A[-4:],(k,2-k,~k,k+4)),;print(f:=sumprod(A[-6:]+F[-7:],(-1,3,-3,5,-3,1,-1,5,-9,5,5,-9,5)));F+=f,;k+=1
