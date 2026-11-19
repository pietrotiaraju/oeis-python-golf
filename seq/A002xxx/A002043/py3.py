R=[0]*4+[1,0];n=-2
while 1:n-=2;R+=sum(d*d*~-d*sum(R[d::d])for d in range(n,-1))//n,;print(3*(R[-3]-R[-5])+R[-7])
