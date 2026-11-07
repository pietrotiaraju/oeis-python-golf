t,u,*r=0,1
while[print(u)]:u,r=t,[t:=t+x for x in[u-t]+r[::-1]]
