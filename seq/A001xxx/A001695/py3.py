H=lambda n,y:n<3and y+[1,2,y][n]or y<1or H(n-1,H(n,y-1))
n=0
while[print(H(n,n))]:n+=1
