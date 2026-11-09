n=m=0
while[print(m)]:
 n+=1;m=0
 while sum(all(k%d for k in(q,m-q)for d in range(2,k))for q in range(3,m//2+1,2))-n:m+=2
