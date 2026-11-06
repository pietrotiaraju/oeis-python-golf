from math import*
a=[1];n=0
while 1:n-=1;a+=sum(d*comb(5-d,6)*sum(a[d::d])for d in range(n,0))//n,;print(a[-1])
