n=3
while[print(sum((n**3-x*x-y*y)**3>=27*(n*x*y)**2*n for y in range(n*n)for x in range(1,y)))]:n+=1