n=X=0
while[print(X)]:n+=1;B=1<<9*n+9;M=B**-~n;V=[1]*5*n;S=0;exec('a=V[1];V[:n+1]=[1+B**k*((V[k]**3+3*V[k]*V[2*k]+2*V[3*k])%M//6)for k in range(n+1)];S+=(V[1]-a)*(V[1]-1);'*-~n);f,g,t,q=V[1:5];X=(B*((f**4+6*f*f*g+8*f*t+3*g*g+6*q)%M//24)-S)%M//B**n
