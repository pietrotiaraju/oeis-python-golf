a=[1];n=0
while[print(sum(map(int.__mul__,(5,2,0,-3,-5,-1,0,3,1,-1),a[::-1])))]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-5)for d in range(n,0))//n,
