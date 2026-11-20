i=0
while 1:
 for h in map(str,range((k:=10**(i//2))-0**i,k*10)):print(h+h[i%2-2::-1])
 i+=1
