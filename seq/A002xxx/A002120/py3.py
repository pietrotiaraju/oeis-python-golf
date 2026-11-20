a=[0];*P,F,n=1,0
while 1:n+=1;P+=F%n*[n];F*=n*n;a[0]=n;a+=-sum(a[-p]for p in P),;print(a[-1]*(-1)**n)
