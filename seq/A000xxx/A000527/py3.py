L=[n:=1,1]
while 1:X=99**n;Q=0;[Q:=Q*X+c for c in L];print(4*Q*(3*Q*Q+8*Q+2)*pow(2-Q,-7,X**n)//X**~-n%X);n+=1;L=[sum(sum(L[d-1::d])*d*L[~d]for d in(1,*range(1,n)))//n]+L
