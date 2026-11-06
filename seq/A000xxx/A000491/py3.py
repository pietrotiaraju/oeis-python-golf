from math import*
a=[1];n=0;F=[];Q=[[0]*k for k in range(1,6)]
while 1:
 t=a[-1]
 for L in Q:t+=L.pop(0);L+=[t]
 F+=[t];print(sum(x*y for x,y in zip([7,5,2,-2,-7,-9,-6,1,4,6,3,1,-3,-2,1],F[::-1])))
 n+=1;a+=[sum((k%2*2-1)*a[-k*(3*k-1)//2]for k in range(-isqrt(n),isqrt(n)+1)if 0<k*(3*k-1)//2<=n)]
