p=11;P=m=1
while 1:
 m+=1
 while any(pow(q,p//5,p)>1for q in range(m+1))or 0in(p%d for d in range(2,4**len(str(p)))):p+=10
 P%m and print(p);P*=m*m
