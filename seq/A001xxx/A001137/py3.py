n=1
while 1:n+=1;s=B=X=3**n;exec('B=(B+B*B)**2%X**-~n;s+=B;'*n);print(s//X**n)
