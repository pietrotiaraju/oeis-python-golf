f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in(3,p%3)for a in range(p-d)if[a%3<1,a//3+p//3&1][d>2]))
N=0
while[print(+f([],0))]:N+=3
