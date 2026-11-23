n=k=1
while 1:
 n+=1;N=(n<<n)-1
 while pow(k*k+4,N//2,N)<2:k+=1
 a,s=2,k;exec('a,s=s,k*s+a;'*2*n+'a=a*a%N-2;'*(n-2));a%N or print(n)
