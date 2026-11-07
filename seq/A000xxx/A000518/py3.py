D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*((7*a*a-u*u)**3+28*a**4*(3*a*a-u*u))-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
