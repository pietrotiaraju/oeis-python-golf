def g(J,L,M,U,t):
 if M.bit_count()>n:
  J=[J[p]|M*(M>>p&1)for p in R];L+=M,;t=~-len(L)//n;M=1<<t;U=J[t]
  if t>n:x=[[max(l*(l>>a&l>>b&1)for l in L)for b in R]for a in R];I=lambda y,f=[],k=0:k==v or any(I(y,f+[c],k+1)for c in{*R}-{*f}if all(x[i-2][j-2]>>R[k-2]&1==y[f[i]][f[j]]>>c&1for j in R[:k]for i in R[:j]));X[:0]=[x][any(map(I,X)):]
 all(U>>c&1or g(J,L,M|1<<c,U|J[c],c)or len(L)//2>n<t for c in R[t+1:])
n=1
while 1:n+=1;R=range(v:=n*n+n+1);X=[];g([0]*v,(),1,0,0);print(len(X))
