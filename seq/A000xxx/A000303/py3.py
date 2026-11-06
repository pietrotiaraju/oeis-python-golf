v=[1,1]
while[print(v[0]-1)]:v=[i*v[i-1]+-~i*sum(v[i:i+2])for i in range(len(v)+1)]