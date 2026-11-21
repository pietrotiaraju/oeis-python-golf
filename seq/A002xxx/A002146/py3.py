P=k=n=1;d={}
while 1:
 a=h=0;c=-P%k*k%8>6
 while 3*a*a<k*c:a+=1;h+=sum((x:=b*b+k>>2)%a<1>a*a-x for b in range(-a|1,a,2))
 d={h:k}|d;P*=k;k+=1
 while n in d:print(d[n]);n+=2
