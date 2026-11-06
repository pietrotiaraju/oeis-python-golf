W=[n:=-1,2]
while[print(sum(map(int.__mul__,W,W[::-1]))//-4)]:W+=sum(d*W[-d]*sum(W[d:0:d])for d in range(n,0))//n,;n-=1
