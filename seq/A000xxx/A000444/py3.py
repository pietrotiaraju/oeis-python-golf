R=[2,1,1];n=3
while 1:S=B=9**n;[S:=(S+c)*B for c in R];print(S**3*(9-8*S+2*S*S)*pow(1-S,-5,B**-~n)//B**n%B);R=[sum(d*R[d]*sum(R[~d::-d])for d in range(-n,0))//-n]+R;n+=1
