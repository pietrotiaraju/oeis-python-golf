f=lambda H,p:p==N or sum(f(H+[x+[-p]],p+1)for x in[[],*H]if all((x<H[a])^(x<H[a+d])==(H[-d]<H[a])^(H[-d]<H[a+d])for d in D for a in range(p-d)if a&d<p&d))
D=[];N=1
while[print(f([],0))]:D+=N,;N*=2
