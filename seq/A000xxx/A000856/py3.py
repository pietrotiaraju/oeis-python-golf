import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or sum(1<<sum(V[::d])//P+d-4for d in(1,2))
n=1;P=2
while[print(f(n,[2]*P))]:n+=1;P*=n
