T=[P:=[n:=0,1]]
while[print(sum(P[-1]-L[-1]for L in T))]:
 n-=1;T+=P[:],;P=-n*[0,0]
 for L in T:L+=sum(d*P[-d]*sum(L[d::d])for d in range(n,0))//n,;P=L
