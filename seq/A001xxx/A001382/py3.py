c=[0]
exec("c=[int(str(x*10+j*100202011222).translate('012'*19))for x in c for j in(0,1,2)];"*12)
for k in range(9):print(sum(len(str(x).replace('0',''))+(x%3>0)==3*k for x in c))
