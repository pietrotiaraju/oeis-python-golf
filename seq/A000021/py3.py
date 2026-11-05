n=0
while[print(len({v for x in range(2<<n//2)for y in range(1<<n//2)if(v:=x*x+12*y*y)<=2**n})-1)]:n+=1
