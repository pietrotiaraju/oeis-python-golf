a=[1];*P,F,n=2,0
while[print(a[-1])]:n-=1;P+=[n][:F%-n];F*=n*n;a+=sum(a[p]for p in P),
