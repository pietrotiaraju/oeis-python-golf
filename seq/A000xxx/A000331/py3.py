K=8**5;a=[0,1<<K];n=1
while[n<4or print(a[n]%2**K)]:n+=1;a+=sum([w:=a[k]*a[-k]>>K,*[w:=w*r+(w>>K)for r in range(1,n)if k%r>n%r]][-1]for k in range(n)),
