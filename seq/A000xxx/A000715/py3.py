*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*sum(a[d::d])*(2+(d>-4))for d in range(n,0))//n,
