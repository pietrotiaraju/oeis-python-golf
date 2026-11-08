n=0
while r:=range(1<<-~n//2|2):print(len({max(x*~x+y*~y,-2**n)for x in r for y in r[:x+1]})-1);n+=1
