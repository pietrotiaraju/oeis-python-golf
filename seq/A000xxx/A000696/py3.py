k=1
while X:=range(k):exec('X={m%2*k+m>>2for m in X};'*k);X-{0}or print(k);k+=2
