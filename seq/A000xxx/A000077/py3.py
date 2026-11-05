n=0
while r:=range(2<<n//2):print(len({min(x*x+6*y*y,2**n+1)for x in r for y in r})-2);n+=1
