n=f=4
while n:=n+1:a=B=n**n;b=3;c=B+2;exec("a,b,c=b,c,(B+2)*c+B*b-a;"*n);print(sum(-~b//B**j%B*(f:=f*j or 1)*(B-1)**(n-j)for j in range(n+1))//B**5%B)
