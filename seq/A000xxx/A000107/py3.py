v=n=0;r=s=1,
while[print(v)]:v=sum(map(int.__mul__,r,s));s=v,*s;n-=1;r+=sum(d*r[~d]*sum(r[d::d])for d in range(n,0))//n,
