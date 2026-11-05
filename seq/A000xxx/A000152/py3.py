m=16
while[print(sum(1<<j*j*m+m for j in range(-m,m))**16>>m*m&2**m-1)]:m+=1
