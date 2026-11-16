T=[P:=[n:=0,1]];s=v=2
while[print(-~-n*v-s+v//2-P[-1])]:
 n-=1;T+=P[:],;P=-n*[0,0];s=0
 for L in T:L+=sum(d*P[-d]*sum(L[d::d])for d in range(n,0))//n,;s+=(v:=2*L[-1]-sum(map(int.__mul__,L,P[::-1]))+n%2*L[1-n>>1]);P=L
