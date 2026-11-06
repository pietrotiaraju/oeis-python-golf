n=1
while r:=range(n):print(len({min((x<<j+n)%n for j in r)for x in r}));n+=1
