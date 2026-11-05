from unicodedata import*
f=lambda n:n>99and f(n//10**(e:=~-len(str(n))//3*3or 2))+'HUNDRED THOUSAND M B TR QUADR QUINT SEXT SEPT OCT NON %UN%DUO%TRE%QUATTUOR%QUIN%SEX%SEPTEN%OCTO%NOVEM%VIGINT'.replace('%','DEC ').split()[e//3]+'ILLION'*(e>3)+f(n%10**e)or n and name(chr([n+119520,n//10+65807][t:=n>19]))[14:]+f(n%10*t)or''
d=1
while[*map(print,sorted(range(d,d*10),key=f)+[0]*(d<2))]:d*=10
