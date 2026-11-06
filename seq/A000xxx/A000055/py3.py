F=1,;n=-1
while[print(F[n]+sum(F[i]*((i-~i==n)-F[n+~i])for i in range(n))//2)]:n+=1;F+=sum(d*F[~d]*sum(F[d::d])for d in range(~n,0))//~n,
