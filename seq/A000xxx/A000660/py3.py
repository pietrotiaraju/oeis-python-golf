r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[len(r)-t]+r[::-1]]
