A=[1]+[0]*7;n=1
while 1:
 n+=1;A+=[0]+[(n-1)*(A[k-4]+A[k-9])for k in range(1,4)]
 if n>5:print(A[-1])
