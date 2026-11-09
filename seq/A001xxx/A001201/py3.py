f=lambda P:P<{1}or sum(f(P-{(i,j),(i,k),(j,k)})for i,j in[min(P)]for k in range(v)if{(i,k),(j,k)}<P)
v=p=1
while[v%6>3or print(p*f({(i,j)for j in range(v)for i in range(1,j)if i+j-v}))]:p*=v;v+=2
