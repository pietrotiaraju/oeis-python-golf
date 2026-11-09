*a,n=1,0
while[print(sum(map(int.__mul__,(3,1,-1,-2,-1,1),a[::-1])))]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-4)for d in range(n,0))//n,
