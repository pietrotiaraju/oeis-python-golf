a=[1];*P,F,n=1,0
while[print(sum(map(int.__mul__,a,a[::-1]))*(-1)**n)]:n+=1;P+=F%n*[n];F*=n*n;a+=-sum(a[-p]for p in P),
