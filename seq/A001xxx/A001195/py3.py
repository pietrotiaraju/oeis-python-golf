h=lambda c,k=9:(11**9)**n*c**k<(14**9*n**10)**n*F**k and-~h(c,k+9)
A=2;F=J=n=1
while 1:
 while(s:=h(A))>h(A+1):J+=1;A=J*A+1;F*=J
 print(+s);n+=1
