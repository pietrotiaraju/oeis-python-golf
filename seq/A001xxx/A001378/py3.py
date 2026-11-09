N=v=0;L=[];K=4308
for c in b"TT'S0m-[=%(`.PBr]eW{122|>E$0GdE=Nv,SpR4S9VwZhC\rMp>$j'd+Qu&!QFTyPhJOgloJl1!|f{vGi;yQQI]Ai Lu{xw!^'gaa9)qhk#c^ayrP	i^tw87uBJ/p~`)MH\\X.fq%5_YaQx+`O1qnASybEUgk:Oml{QQ^dmJO?bG\0{W#2$nO1I}y!AZTO5RK`kJ'Lh{\"@={43gKeDJk0TPNQ#h	}0d	z$3|EV\\U9Y/,\rw(>kigv!ZFsL'Dc#]8/<Q?G7~k#I`!w6_Lsi?/Z?ZQi\r)<Fv{mv}^ow:o'@":N=N*128+c
while N>1:
 while N%2:v+=K;N//=2
 v+=N//2%K;N//=2*K;x=1;y=v
 for p,r in zip(b'\r/',b'('):x*=p**(y%r);y//=r
 L+=x,
print(*sorted(L),sep='\n')
