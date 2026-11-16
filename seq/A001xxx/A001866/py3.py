n=0;f=1
while 1:s=i=0;exec('s=(s+n**i//n)*i;i+=1;'*n);print(f*s//2);n+=1;f*=n
