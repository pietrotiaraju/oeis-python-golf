a=[1];*P,F,n=1,0
while[print(a[-1])]:n-=1;P+=F%-n*[n];F*=n*n;a+=sum(d*sum(a[d::d])for d in P)//n,
