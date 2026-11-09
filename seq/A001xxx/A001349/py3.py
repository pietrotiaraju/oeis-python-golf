import math,functools as F
f=F.cache(lambda r,*L:r<1or sum(f(r+k,*sorted(L+(k,)))<<-k//2+sum(map(math.gcd,L,[k]*n))for k in range(-r,0))//r)
R=C=1,;n=1
while[print(C[-1])]:R=f(n),*R;C+=R[0]-sum(d*C[d]*sum(R[d::d])for d in range(1,n))//n,;n+=1
