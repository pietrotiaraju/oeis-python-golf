a=[1];n=b=c=0;Q=[0]*2,[0]*3
while 1:
 b+=a[-1];c+=b;t=b
 for L in Q:L+=[t:=t+L.pop(0)]
 print(b+c+t)
 n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
