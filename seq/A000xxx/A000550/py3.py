*L,n=1,1,0;Z=0,
while[n>-16or print((sum(map(int.__mul__,Z,Z[::-1]))+Z[-n//2])//2)]:
 n-=2;Z+=0,L[-2]-L[-1]
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
