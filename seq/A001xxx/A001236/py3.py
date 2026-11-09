x=y=z=f=1;N=2
while[print(z:=N**3*z+f*(y:=N*N*y+f*(x:=N*x+f)))]:f*=N;N+=1
