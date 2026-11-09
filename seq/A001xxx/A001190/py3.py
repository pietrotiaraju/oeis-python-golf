L=[0,1]
for x in L:print(x);n=len(L);L+=(sum(map(int.__mul__,L[1:],L[:0:-1]))+~n%2*L[n//2])//2,
