n=3
while F:={r:=n**49}:
 for x in range(-n**74,0,n**72):
  while r**3>x*x:r=(2*r+x*x//r//r)//3
  F|={r}
 print(sum(a<=b<=c<=r*n-a-b for a in F for b in F for c in F));n+=1
