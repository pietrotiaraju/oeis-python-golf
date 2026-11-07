t=0;r=[1]
while[print(t)]:exec("r=[2*(t:=t+x)for x in[-t]+r[::-1]];"*2)