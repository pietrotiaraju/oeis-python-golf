n=0
while 1:
 N=n;F=d=1
 while -(2*N+F)%(2*F)<2*n**d:d+=2;N=N*d*(d-1)+n**d;F*=d*(d-1)
 print((2*N+F)//(2*F));n+=1
