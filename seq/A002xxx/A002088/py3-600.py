s=0;n=F=1
while[print(s)]:s+=sum(1%n==pow(k,F,n)for k in range(n));n+=1;F*=n
