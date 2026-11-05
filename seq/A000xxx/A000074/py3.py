n=0
while r:=range(2<<n//2):print(len({max(x*~x+y*~y,-2**n)for x in r for y in r})-1);n+=1
