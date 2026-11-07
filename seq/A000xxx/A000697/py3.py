r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[len(r)**2-t]+r[::-1]]
