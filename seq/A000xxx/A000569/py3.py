def P(n,m=1):return[()]if n==0 else[(j,)+p for j in range(m,n+1)for p in P(n-j,j)]
def f(p):
 p=sorted(p,reverse=True)
 return not p or p[0]<len(p)and f([x-(i<p[0])for i,x in enumerate(p[1:])if x-(i<p[0])])
n=0
while 1:n+=1;print(sum(map(f,P(2*n))))
