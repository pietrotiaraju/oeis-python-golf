P=k=1
while 1:
 if-P%k*k%4>2:
  a=h=0
  while 3*a*a<k:a+=1;h+=sum((x:=b*b+k>>2)%a<1>a*a-x for b in range(-a|1,a,2))
  print(h)
 P*=k;k+=1
