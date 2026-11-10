f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in{n,1}-{p%n<1}for a in range(p-d)if(a//d%n+p//d%n)%2*(~a//d%n)))
n=1
while[N:=n*n,print(f([],0))]:n+=1
