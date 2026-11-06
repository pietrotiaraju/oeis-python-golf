a=[0,n:=1]
while[print(a[n])]:n+=1;a+=sum(max(w:=a[k]*a[-k],*[w:=w*r**(k%r>n%r)for r in range(1,n)])for k in range(n)),
