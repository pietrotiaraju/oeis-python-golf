R=lambda a,b,c:{(a,b):c,(b,c):a,(c,a):b}
def C(N):
 for s in 1,-1:
  for a,b in N:
   D={a:0};Q=[(a,b,b)];c=[]
   for x,y,z in Q:
    while(z:=N[(x,z)[::s]])!=y:Q+=[(z,x,x)][z in D:];c+=D[x],D.setdefault(z,len(D))
   yield c
T=R(0,1,2)|R(1,0,2);S=[]
while[print(len(S)or 1)]:
 (u,v),w=T.popitem();T|=R(u,v,k:=len(T))|R(v,w,k)|R(w,u,k);S=[];Q=[T]
 for T in Q:
  for u,v in T:
   if(x:=T[u,v],y:=T[v,u])not in T:
    M=T|R(x,u,y)|R(y,v,x);del M[u,v],M[v,u]
    if(k:=min(C(M)))not in S:S+=k,;Q+=M,
