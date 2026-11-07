r=[0,t:=1]
while[print(t-2*r[1])]:r=[t:=t+x for x in[-t]+r[::-1]]