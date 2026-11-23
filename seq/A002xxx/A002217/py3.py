S=[0,0];A=[0,2];n=1
while[print(A[n])]:
 n+=1;d=2
 while n%d:d+=1
 S+=d+S[n//d],;A+=A[S[n]%n]+1,
