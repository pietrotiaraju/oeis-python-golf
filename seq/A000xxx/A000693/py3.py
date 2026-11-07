n=p=1
while r:=range(2<<n//2):print(p:=len({min(x*x+y*y,2**n)for x in r for y in r})+~p);n+=1
