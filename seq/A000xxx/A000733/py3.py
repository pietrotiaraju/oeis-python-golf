n=0;r=a=[t:=1]
while[print(t)]:r=[t:=t+x for x in[a[-1]-t]+r[::-1]];n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,