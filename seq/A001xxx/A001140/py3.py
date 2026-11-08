import re
s='4'
while[print(s)]:s=re.sub(r'(.)\1*',lambda m:str(len(m[0]))+m[1],s)
