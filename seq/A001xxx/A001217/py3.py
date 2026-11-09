S={1,12,1152,51840,2903040,696729600}
k=f=1
while[print(v)for v in sorted(S)if k>=v//f>0]:k+=1;f*=k;S|={f,f<<k,f<<k-1}
