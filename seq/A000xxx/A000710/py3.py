*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-5)for d in range(n,0))//n,
