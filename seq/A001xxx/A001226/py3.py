t=F=1
while[print(~-2**sum(1%t==pow(k,F,t)for k in range(t))//t)]:F*=t*-~t;t+=2
