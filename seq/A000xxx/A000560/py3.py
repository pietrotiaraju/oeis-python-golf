L=[[n:=1]],
while[n<3or print(len(L)//n//2)]:L=[(x+[-n],p,*r)for p,*r in L for x in([],p,*r)if all((x<c)^(x<d)==(p<c)^(p<d)for c,d in zip(*[iter(r)]*2))];n+=1
