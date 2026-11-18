n=0
while 1:Q=(n+2)**8;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*8);print(V//Q**(4*n)%Q);n+=1
