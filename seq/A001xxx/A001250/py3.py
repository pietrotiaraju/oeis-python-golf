r=[t:=1]
while[print(sum(r[-2:]))]:r=[t:=t+x for x in[-t]+r[::-1]]
