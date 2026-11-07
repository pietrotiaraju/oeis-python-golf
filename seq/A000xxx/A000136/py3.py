L=[[0]],
while[print(n:=len(L))]:L=[(x+[-n],p,*r)for p,*r in L for x in([],p,*r)if all((x<c)^(x<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))]