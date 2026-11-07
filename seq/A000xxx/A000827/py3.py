import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or sum(d**3%5<<sum(V*(3-d)+V[::d]*d)//P for d in(1,2,3))
n=1;P=6
while[print(f(n,[1]*P)//6)]:n+=1;P*=n
