a=[1];n=c=0;Q=[[0]*k for k in range(1,5)]
while t:=a[-1]:
 T=[L.append(t:=t+L.pop(0))or t for L in Q]
 print((c:=c+(b:=T[0]+T[1]))+b+t)
 n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
