n=8
while[print((1-(x:=8**n))**-~n*sum(j**n*x**j for j in range(9))//x**8%x)]:n+=1
