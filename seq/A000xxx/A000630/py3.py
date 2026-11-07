d={0:1};n=0
while[print(d[n])]:n+=1;d[n]=sum(d[j]*d.get(n-2**j,0)for j in d)
