*r,p=1,
while[*map(print,r),k:=4*len(r)]:r=[p+(p:=x)*(k:=k-1)for x in r+[0]]