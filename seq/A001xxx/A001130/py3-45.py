r=lambda j,t,D,E:D+j*t<=E and sum(r(j-1,u,max(D+u,0),E-j*abs(u-t))for u in range(t-E//j,t+E//j+1))if j else E|D<1
n=2
while[print(sum(r(d,1,0,n-d*d)for d in range(n)))]:n+=2
