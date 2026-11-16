r=[0,2,12,10,0,0];n=4
while 1:n+=1;r=[k*r[k]+2*r[k-1]+(n-k)*r[k-2]for k in range(n)]+[0,0];print(r[-6])
