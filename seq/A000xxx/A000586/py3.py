*a,n=1,0;*P,t=1,
while[print(a[-1])]:n+=1;P+=t%n*[-n];t*=n*n;a+=sum(p*(sum(a[p::2*p])-sum(a[2*p::2*p]))for p in P)//-n,
