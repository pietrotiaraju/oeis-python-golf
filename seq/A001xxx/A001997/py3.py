n=s=1
while[print(s)]:
 s=0
 for N in range(3**n//6+1):
  p=d=1;E={1};k=N;r=0
  for _ in[0]*~-n:t=k-(k:=(k+1)//3)*3;r=3*r+t;d*=1j**t;E|={2*p+d};p+=d
  s+=n-len(E)<1>r*r-N*N
 n+=1
