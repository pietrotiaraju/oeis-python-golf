import math
f=lambda r,V:r and sum(f(r+~k,[V[t]<<math.gcd(t,~k)for t in range(P)])for k in range(r))//r or 1<<sum(V)//P-3
n=P=1
while[print(f(n,[3]*P))]:n+=1;P*=n
