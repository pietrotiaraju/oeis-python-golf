r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[r[0]-(r*2)[-2]]+r[::-1]]