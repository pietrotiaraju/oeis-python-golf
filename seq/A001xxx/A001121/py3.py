def T(r,j,Z,E):
 if~Z&K:0
 elif j<N:
  for v in(1,-1)[S[r][j-1]<0<(E[j-1]==E[j]):]:S[r][j]=v;S[j][r]=-v;T(r,j+1,Z-(E[j]<<N*(v<0)),E)
 else:
  R[r:]=[sum(2**j for j in W if S[r][j]<0)];I={};U=lambda i,B:all(I.setdefault(i,v:=[(x&X).bit_count()for X in B])<v or v==I[i]and U(i+1,[y for X in B for y in(X&~x-2**c,X&x)if y]+[0])for c,x in enumerate(R)if B[0]>>c&1)
  if U(0,[~-2**N]):T.n+=r>N-2;~r+N and T(q:=r+1,q+1,K+sum(c<<N*i for i,c in enumerate(c for m,b in[(N+~q,sum(S[q][1:q]))]for s in S[:q]for a,g in[(sum(map(int.__mul__,S[q],s[:q])),sum(s[q+1:]))]for c in(m+g-b-a,m+g+b+a,m-g-b+a,m-g+b-a))),[sum(4<<N*(4*k+1-s[j])for k,s in enumerate(S[:q]))for j in W])
N=8
while 1:W=range(N);S=[[(i<1)-(j<1)for j in W]for i in W];T.n=0;K=~-2**(4*N*N)//~-2**N<<N-1;R=[];T(0,N,K,0);print(T.n);N+=4
