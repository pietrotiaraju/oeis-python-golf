n=7
while[print((1-(x:=8**n))**-~n*sum(j**n*x**j for j in range(8))//x**7%x)]:n+=1
