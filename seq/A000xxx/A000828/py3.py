r=[t:=1]
while[print(t)]:r=[2*(t:=t+x)for x in[-t]+r[::-1]]