a=4;b=2;c=d=k=1
while a//c-b//d or[print(a//c),c:=a%(a:=c),d:=b%(b:=d)]:exec("a,b,c,d=c,d,2*k*a+b,k*a-~k*b;"*2);k+=1
