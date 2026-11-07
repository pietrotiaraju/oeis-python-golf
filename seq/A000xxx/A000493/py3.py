s=lambda t,d=1:t and t+s(t*d//(d-~d),d+1)
n=j=0
while 1:
 j+=1;p=2*s(S:=2**j)
 while(q:=n*S//(p+8*j))==n*S//p:print(q%-2);n+=1
