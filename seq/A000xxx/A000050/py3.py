n=0
while r:=range(1<<-~n//2|3):print(len({min(x*x+y*y,2**n)for x in r for y in r})-1);n+=1
