q=t=l=y=1
while(y-q)*(c:=t//y+1)<t or[print(c),y:=y*c-t,q:=q*c,t:=t*c]:l+=2;y=y*l-2*q;q*=l//2;t*=l
