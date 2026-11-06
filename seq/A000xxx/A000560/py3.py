L=[[0]],
n=1
while 1:
 if n>2:print(len(L)//(2*n))
 L=[(x+[-len(q)],*q)for q in L for x in([],*q)if all((x<c)^(x<d)==(q[0]<c)^(q[0]<d)for c,d in zip(q[1::2],q[2::2]))];n+=1
