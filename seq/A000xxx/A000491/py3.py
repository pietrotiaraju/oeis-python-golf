a=[1];n=c=0;Q=[[0]*k for k in range(1,6)]
while t:=a[-1]:
 T=[L.append(t:=t+L.pop(0))or t for L in Q]
 print(T[0]+(c:=c+2*sum(T[:2])+T[2])+t)
 n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
