r=[t:=1]
while[print(t>>len(r)-1)]:s=sum(r);t=0;r=[t:=t+(s:=s-x)+x for x in[0]+r]
