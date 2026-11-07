*r,n=0,1,1,2,4,-3
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];U=X**-~-n-T;print(T**5*(((15*T+85*U)*T+171*U*U)*T+125*U**3)//U**7%X)
