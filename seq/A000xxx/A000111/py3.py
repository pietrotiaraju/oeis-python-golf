r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[-t]+r[::-1]]
