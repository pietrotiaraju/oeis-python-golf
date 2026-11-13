j=0
while[*map(print,sorted({m**k for m in range(2<<j)for k in range(2,2*j+3)if 0<m**k>>2*j<4}))]:j+=1
