m=k=0;N=29
while 1:
 while pow(k*k+4,N//2,N)<2:k+=1
 a,s=2,k;exec('a,s=s,k*s+a;'*30+'a=a*a%N-2;'*m);(a+2)%N or print(m+1);m+=1;N-=~N
