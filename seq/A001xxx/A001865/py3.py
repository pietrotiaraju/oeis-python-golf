n=0
while 1:n+=1;s=i=0;exec('s=s*i+n**i;i+=1;'*n);print(s)
