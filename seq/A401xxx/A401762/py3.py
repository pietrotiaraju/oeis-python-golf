f=lambda n,Q=0,t={},p=0,U=b';<<E2@':n<1or sum(f(n-1,c&1,t|{p:U[c&6:][:2]},p+c%5-2)for c in t.get(p,U)[Q::2])
n=1
while 1:print(f(n)+f(n,1));n+=1
