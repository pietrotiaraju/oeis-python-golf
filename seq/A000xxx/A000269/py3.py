*r,n=1,1,2
while 1:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;n+=1;X=8**n;T=0;[T:=T*X+c for c in r];print(T**3*(T+3*(U:=X**n-T))//U**3%X)
