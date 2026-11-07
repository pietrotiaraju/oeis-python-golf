Q=1,;n=0
while 1:Q+=0,0,0,sum(map(int.__mul__,Q[::4],Q[2*n::-2]));n+=1;print((Q[-1]+Q[2*n]+Q[n-1])//2)
