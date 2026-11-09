c=1;m=0
while 1:s=0;print(sum((c:=c*(j-m-2)//j)//j*(s:=s-j**m)for j in range(1,m+2)));m+=2;c*=m*~m
