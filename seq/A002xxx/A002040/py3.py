H=[t:=1]
while[print(H[-1])]:H+=sum((1-(j&2))*~-g*H[g]for j in range(-t,t)if~t<(g:=j-j*3*j+2>>1)<0),;t+=1
