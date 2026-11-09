a=1;t=0
while[print(a)]:a=t+(t:=sum(d*(a%d<1)for d in range(1,a+1)))
