import math
a=[1];b=[0]
while 1:
 n=len(a);b+=[sum(k*math.comb(k+5,6)for k in range(1,n+1)if n%k<1)]
 a+=[sum(b[k]*a[n-k]for k in range(1,n+1))//n];print(a[-1])
