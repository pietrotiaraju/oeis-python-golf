f=lambda a,r,b,s,t:a+r>m or f(a+1,r+(t==r),b,s,t+1)+f(b+1,s,a,r,1)
m=1
while[print(+f(1,1,0,1,1))]:m+=2
