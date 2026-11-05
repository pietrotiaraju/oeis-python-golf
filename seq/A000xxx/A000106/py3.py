F=[1];n=0
while[print(sum(map(int.__mul__,F,F[::-1])))]:n-=1;F+=sum(d*F[~d]*sum(F[d::d])for d in range(n,0))//n,
