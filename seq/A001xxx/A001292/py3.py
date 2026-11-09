l=[]
while 1:l+=str(len(l)+1),;[*map(print,sorted(''.join(l:=l[1:]+l[:1])for x in l))]
