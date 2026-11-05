n=2
while[print(sum((n**3-x*x-y*y)**3>=27*(n*x*y)**2*n for y in range(n*n)for x in range(-y,0)))]:n+=1
