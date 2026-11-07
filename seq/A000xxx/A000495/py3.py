n=0
while 1:
 M=d=1;G=2
 while-M%G<2*n**d:M=M*d+2*n**d*(d&1);G*=d;d+=1
 print(M//G);n+=1
