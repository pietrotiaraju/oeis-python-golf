V=[(1,0),(-1,1),(0,-1)]
def f(x,y,d,n,S):
 if n==0:return 1
 t=0
 for j in(d,(d+1)%3):
  a=x+V[j][0];b=y+V[j][1]
  if(a,b)not in S:S.add((a,b));t+=f(a,b,j,n-1,S);S.remove((a,b))
 return t
n=0
while 1:print(f(1,0,0,n-1,{(0,0),(1,0)})if n else 1);n+=1
