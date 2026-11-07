*a,n=1,0;t=1;P=[]
while[print(a[-1])]:n+=1;P+=[-n][:t%n];t*=n*n;a+=sum(p*(sum(a[p::2*p])-sum(a[2*p::2*p]))for p in P)//-n,
