n=0
while 1:B=X=3**n;s=0;exec('B=(B+B*B)%X**-~n;s+=B;B*=B;'*n);print(s//X**n);n+=1
