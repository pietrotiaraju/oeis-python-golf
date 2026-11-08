Y=int.bit_count
K=lambda v,r:[S[v][:r]]+sorted(s[:r]+[s[v]]for s in S[r:])
def D(P,B,Q):
 if(d:=len(P))==N:
  if Q<b[0]:b[:]=Q,P;return
  G.append({x^e:y^e for x,y in zip(b[1],P)for e in(0,1)});return 1
 L=[(R[u]^R[[*P,2*u][0]>>1]^F*e,2*u+e)for u in{*W}-{q>>1for q in P}for e in(0,1)]
 for X in B:z=min(Y(x&X)for x,p in L);Q+=z,;L=[c for c in L if Y(c[0]&X)==z]
 E={-1};n=len(G)
 if Q>b[0]:return
 for x,p in L:
  O={p}
  for _ in L:O|={g[o]for o in O for g in G[n:]}
  if not O&E and D(P+(p,),[y for X in B for y in(X&~x,X&x)if y],Q)and P!=b[1][:d]:return 1
  E|=O
def T(r,j,A):
 global R,G,b
 if j<N:
  for v in(1,-1)[S[r][j-1]<0<(S[j-1][:r]==S[j][:r]):]:S[r][j]=v;S[j][r]=-v;max(map(abs,B:=[a+v*s[j]for a,s in zip(A,S)]))<N-j and T(r,j+1,B)
 elif~r+N:T(q:=r+1,r+2,[sum(map(int.__mul__,S[q][:q],s))for s in S[:q]])
 elif all(K(j,r)>=K(r,r)for r in W for j in W[r:])>any(A):R=[sum(2**j for j in W if s[j]<0)for s in S];G=[];b=[(N,)]*2;D((),[F],());C[b[0]]=0
N=8
while 1:W=range(N);S=[[(i<1)-(j<1)for j in W]for i in W];C={};F=2**N-1;T(1,2,[0]);print(len(C));N+=4
