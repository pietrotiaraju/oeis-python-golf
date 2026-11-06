R=[n:=-1,0,1]
while[print(sum(map(int.__mul__,R,R[::-1]),R[-n])//-2)]:R+=0,sum(d*(R[-d-d]-R[-d])*sum(R[d-~d:0:d+d])for d in range(n,0))//n;n-=1
