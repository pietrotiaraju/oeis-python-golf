from math import*
a=[1];n=0;F=[0]*15;Q=[[0]*k for k in range(1,6)]
while 1:
 t=a[-1]
 for L in Q:L+=[t:=t+L.pop(0)]
 F=[t]+F;print(sumprod([7,5,2,-2,-7,-9,-6,1,4,6,3,1,-3,-2,1],F[:15]))
 n+=1;a+=[sum((k%2*2-1)*a[-k*(3*k-1)//2]for k in range(-isqrt(n),isqrt(n)+1)if 0<k*(3*k-1)//2<=n)]
