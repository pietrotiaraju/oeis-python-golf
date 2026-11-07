*a,n=1,0;b=[]
while[print(x:=a[-1]-sum(b[d]for d in range(1,-n)if n%d<1))]:b+=x,;n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
