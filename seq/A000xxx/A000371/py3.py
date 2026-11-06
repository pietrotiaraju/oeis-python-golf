r=[t:=2]
while[print(t)]:r=[t:=r[0]**2]+[t:=t-x for x in r]
