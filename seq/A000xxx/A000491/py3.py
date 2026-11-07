*a,n=1,0;Q=[k*[0]for k in range(1,6)]
while t:=a[-1]:
 for L in Q:L+=(t:=t+L.pop(0)),
 print(sum(sum(Q[:4]+Q[1:3],[t])));n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
