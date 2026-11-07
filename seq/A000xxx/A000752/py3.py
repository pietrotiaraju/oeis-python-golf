r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[2*r[0]-t]+r[::-1]]
