t=k=P=1;r=[]
while~P%k or[r:=[t:=t+x for x in[k-t]+r[::-1]],print(t)]:P*=k;k+=1