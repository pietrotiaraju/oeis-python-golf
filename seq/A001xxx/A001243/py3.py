n=7
while[c:=1,print(sum((c:=c*(j+~n)//-~j)*(6-j)**n for j in range(6))+7**n)]:n+=1
