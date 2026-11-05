R=lambda a,b,c:{(a,b):c,(b,c):a,(c,a):b}
def l(s,D,L):
 for a,b in D:
  for _ in D:D+=[(b,a)][b in L:];L+=b,;b=F[(a,b)[::s]]
 return*map(L.index,L),
n=1
while Q:=[G:={}]:
 S={N:=0}
 for i in range(n:=n+1):G|=R(n,i-1,i)|R(-1,i+1,i)
 for F in Q:
  if{c:=min(l(s,[d],[])for s in(1,-1)for d in F)}-S:S|={c};N+=c[3]>0;Q+=[{k:F[k]for k in F if{*k}^{u,v}}|R(x,u,y)|R(x,y,v)for u,v in F if(u<v)>((x:=F[u,v],y:=F[v,u])in F)]
 print(N)
