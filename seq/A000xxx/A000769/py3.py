f=lambda P,r=0:r==n!=(Q:=P)and sum({*(Q:=[[(y,x),(n+~x,y)][i%2]for x,y in Q])}=={*P}for i in b'01'*4)or sum(f(P+[(r,a),(r,b)],r+1)for a in range(n)for b in range(a)if len({(c,(y-c<<n)//(r-x))for c in(a,b)for x,y in P})==4*r)
n=1
while[print(f([])//8)]:n+=1
