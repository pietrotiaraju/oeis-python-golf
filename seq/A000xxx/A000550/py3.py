*L,n=1,1,0;R=0,0
while[n>-14or print((sum(map(int.__mul__,R,R[::-1]))+n//2%2*R[-n//4+1])//2)]:
 n-=2
 for h in 1,0:L+=sum(d*L[~d*h]*sum(L[d::d])for d in range(n,0,2))//n,
 R+=L[-2]-L[-1],
