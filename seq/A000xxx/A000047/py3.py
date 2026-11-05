n=0
while r:=range(2<<n//2):print(len({v for x in r for y in r if~-(v:=2*y*y-x*x)>>n==0}));n+=1
