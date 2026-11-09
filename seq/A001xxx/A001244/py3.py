n=8
while[c:=1,print(sum((c:=c*(j+~n)//-~j)*(7-j)**n for j in range(7))+8**n)]:n+=1
