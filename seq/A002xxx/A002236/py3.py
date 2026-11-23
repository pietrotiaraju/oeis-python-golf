m=k=0;N=17
while 1:
 while pow((s:=k*k+2)+2,N//2,N)<2:k+=1
 exec('s=s**3-3*s;'*2+'s=s*s%N-2;'*m);(s+2)%N or print(m+1);m+=1;N-=~N
