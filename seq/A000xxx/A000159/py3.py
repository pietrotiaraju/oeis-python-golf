a=1;b=c=0;n=3
while[print(n*abs(2*(a+c)+~b)*2//3)]:a,b,c=b,c,~-n*(b-c)-a;n+=1
