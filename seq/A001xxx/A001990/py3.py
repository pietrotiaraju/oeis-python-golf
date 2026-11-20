r=5;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,
  while any(pow(-2*r,d//2,d)<2for d in Q)or 0in(r%d for d in range(2,r//q)):r+=24
  print(r)
 P*=q*q;q+=1
