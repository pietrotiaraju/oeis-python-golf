D=[a:=0]
while 1:a+=1;D+=sum((u:=abs(y*y%(4*a)-2*a)-a)*(427*a**6-175*a**4*u*u+21*a*a*u**4-u**6)-D[a//y]*(y%2>a%y)for y in range(2,2*a+2)),;print(D[a]>>1%a)
