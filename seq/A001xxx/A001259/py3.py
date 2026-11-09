P=1;p=3
while[P%(p-2)+pow(2*P,p,p-1)or any(p%d<1for d in range(2,p))or[print(p),P:=P*p]]:p+=2
