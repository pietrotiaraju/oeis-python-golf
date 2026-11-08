m=0;F=b=c=p=q=1
while 1:c,b,p,q=b,2*b+m*c,q,m*p;m+=2;F*=m;print(F-b-q>>2)
