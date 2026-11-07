*r,n=0,1,1,2,-2
while 1:n-=1;r+=sum(d*r[-d]*sum(r[d::d])for d in range(n,0))//n,;X=99**-n;T=0;[T:=T*X+c for c in r];V=X**-~-n;print(V*T**4*(((64*V-79*T)*V+36*T*T)*V-6*T**3)//(V-T)**7%X)
