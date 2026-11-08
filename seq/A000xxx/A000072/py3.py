n=0
while r:=range(1<<-~n//2|3):print(len({min(x*x+y*y,2**n+1)for x in r for y in r[::2]})-2);n+=1
