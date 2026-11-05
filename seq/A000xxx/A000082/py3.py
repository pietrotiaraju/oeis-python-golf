k=1
while 1:a=n=k;P=k=1;exec("P*=k*k;k+=1;a+=(P%k>n%k)*a//k;"*n);print(a*n)
