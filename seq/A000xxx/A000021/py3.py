n=0
while[print(len([r:=range(2<<n//2)]and{v for x in r for y in r if(v:=x*x+12*y*y)<=2**n})-1)]:n+=1
