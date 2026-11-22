r=[1];D={}
for n in r:r+=n+1,;D={sum(d*(n%d<1)for d in r):n,**D};n in D!=print(D[n])
