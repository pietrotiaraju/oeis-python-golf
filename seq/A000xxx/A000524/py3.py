r=[n:=0,1]
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];V=X**-~-n;print(V*T*T*(2*V-T)//(V-T)**3%X)
