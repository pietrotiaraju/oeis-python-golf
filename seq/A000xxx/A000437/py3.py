n=1;c=[k:=0]
while 1:
 for x in range(k+1):
  for y in range(x+1):c[x*x+y*y+k*k]+=1
 k+=1;c+=[0]*6*k;n+=n in c[:k*k]!=print(c.index(n))
