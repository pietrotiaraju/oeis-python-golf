H=[t:=1]
while[print(H[-1])]:H+=sum(~-(j&2)*H[g]*(5*g+t)for j in range(-t,t)if~t<(g:=j-j*3*j+2>>1)<0)//t,;t+=1
