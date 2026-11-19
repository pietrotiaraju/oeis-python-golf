n=0
while 1:Q=(n+2)**7;V=x=1;exec("x*=Q;V*=x*Q**n-1;V//=~-x;"*7);print(V//Q**(7*n//2)%Q);n+=1
