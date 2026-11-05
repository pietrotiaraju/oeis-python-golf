d={1:1};n=5
while k:=n//2:d[k]=d[k-1]*(4*k-6)//k;print(d[k]-d.get(n/4,0)-d.get(n/6,0));n+=1
