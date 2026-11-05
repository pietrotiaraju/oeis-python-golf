m=8
while[print(sum(1<<j*j*m+m for j in range(-m,m))**8>>m*m&2**m-1)]:m+=1