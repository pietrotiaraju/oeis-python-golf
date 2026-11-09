g=[1]*5;f=1;N=2
while 1:s=t=1;g=[s:=(t:=t*N)*x+f*s for x in g];print(s);f*=N;N+=1
