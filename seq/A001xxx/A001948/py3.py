f=lambda n,k,j=4:any(f(n-i*i,i,j-1)for i in range(k*(n>=0<j)))or n|j==0
n=0
while[f(n,n)<1<=n%4==print(n)]:n+=1
