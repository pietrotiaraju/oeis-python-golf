f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in(2,p%2)for a in range(p-d)if a&d^p&d))
N=0
while[print(+f([],0))]:N+=2
