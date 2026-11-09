p=int.bit_count
g=lambda d,L,k,U,X:any(k<2or g(d-w,[c for c in L[L.index(R):]if max(p(c&R&r)for r in X)<3>d-~-~w-k*w-p(c)],k-1,U|R^R*2,X+[R])for R in L if d<=k*(w:=p(R))>>(R*2&~(R|U)))
n=c=2
while 1:
 n+=1
 while g(c,sorted(range(2**n),key=p)[::-1],n,2**n,[0]):c+=1
 print(c)
