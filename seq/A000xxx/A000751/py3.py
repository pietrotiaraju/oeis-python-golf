n=0;r=a=[t:=1]
while[print(t)]:n-=1;r=[t:=t+x for x in[sum(d*sum(a[d::d])for d in range(n,0))//n-t]+r[::-1]];a+=r[:1]
