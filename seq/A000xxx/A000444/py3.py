R=[2,1,1];n=3
while 1:S=B=9**n;[S:=S*B+c for c in R];U=pow(1-S*B,-1,B**-~n)-1;print(U**3*(3*U*U+10*U+9)//B**n%B);R=[sum(d*R[d]*sum(R[~d::-d])for d in range(-n,0))//-n]+R;n+=1
