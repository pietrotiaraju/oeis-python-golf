P=m=1;a=[1]
while 1:a+=2*sum(d*sum(a[d::d])<<(d%11<1)for d in range(-m,0))//m,;P*=m*m;m+=1;P%m and print(a[-1])
