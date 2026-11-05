n=1
while[print(next((b for b in range(2,11)if(m:=sum(n//b**i%b*10**i for i in range(n)))*all(m%d for d in range(2,m))>1),0))]:n+=1
