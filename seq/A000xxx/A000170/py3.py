f=lambda c,d,e:c+1>>n or sum(f(c|b,(d|b)*2,(e|b)//2)for i in range(n)if(b:=1<<i)&~(c|d|e))
n=0
while[print(f(0,0,0))]:n+=1
