r=[t:=1]
while[r<[t%2]or print(t)]:r=[t:=t+x for x in[-t]+r[::-1]]
