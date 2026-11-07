r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[1//t-t]+r[::-1]]
