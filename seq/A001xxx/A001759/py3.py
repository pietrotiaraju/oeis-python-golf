r=[0,2,n:=4,0,0]
while 1:r=[k*r[k]+2*r[k-1]+(n-k)*r[k-2]for k in range(n)]+[0,0];print(r[-5]);n+=1
