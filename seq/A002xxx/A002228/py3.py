p=23;P=m=1
while 1:
 m+=1
 while any(pow(q,p//11,p)>1for q in range(m+1))or 0in(p%d for d in range(2,4**len(str(p)))):p+=22
 P%m and print(p);P*=m*m
