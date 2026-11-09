p=int.bit_count
g=lambda d,L,k,U:any(k<2or g(d-w,[c for c in L[:L.index(R)]if p(c&R)<2>d-~w-k*w-p(c)],k-1,U|R^R*2)for R in L[::-(k<n)|1]if d<=k*(w:=p(R))>>(R*2&~(R|U)))
n=c=1
while 1:
 n+=1
 while g(c,sorted(range(2**n),key=p),n,2**n):c+=1
 print(c)
