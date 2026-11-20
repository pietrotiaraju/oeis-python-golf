*Q,F,n=1,1,0
while[print(Q[n]-0**n)]:n+=1;k=F%n*n;Q=[x+k*y for x,y in zip(Q+[0]*n,[0]*n+Q)];F*=n*n
