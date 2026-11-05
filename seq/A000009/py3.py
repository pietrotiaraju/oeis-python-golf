p=[1];k=0
while[print(p[k])]:k+=1;p=[*map(sum,zip(p+[0]*k,[0]*k+p))]
