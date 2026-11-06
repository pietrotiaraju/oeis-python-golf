*R,n=1,0
while[print(R[-1])]:n-=2;R+=sum(d*d*~-d*sum(R[d::d])for d in range(n,0))//n,
