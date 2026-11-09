n=0
while 1:
 n+=1;t=0;r=range(N:=n*n);L=[sum(1<<j for j in r if 0in(u:=j//n-i//n,v:=j%n-i%n,u+v,u-v))for i in r]
 g=lambda i,a,m:N-a.bit_count()>t and(m<1or any(g(s+1,a|L[s],m-1)for s in range(i,N)))
 while g(0,0,n):t+=1
 print(t)
