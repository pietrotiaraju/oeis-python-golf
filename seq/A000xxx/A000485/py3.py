r=[n:=1]
while 1:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;n+=1;X=8**n;T=0;[T:=T*X+c for c in r];U=X**n-T;n>3==print(T**4*(3*T*T+13*T*U+16*U*U)//U**5%X)
