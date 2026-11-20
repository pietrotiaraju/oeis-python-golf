r=5;P=4;q=3;Q=[]
while 1:
 if P%q:
  Q+=q,;a=h=0
  while any(pow(-2*r,d//2,d)<2for d in Q)or 0in(r%d for d in range(2,r//q)):r+=24
  while a*a<3*r:a+=1;h+=sum((x:=b*b+8*r>>2)%a<1>a*a-x for b in range(a%2-a,a,2))
  print(h)
 P*=q*q;q+=1
