# A001378

> Degrees of irreducible representations of Baby Monster group B.
> — [OEIS A001378](https://oeis.org/A001378)

Offset 1: 1, 4371, 96255, 1139374, 9458750, 9550635, 63532485, 347643114, …

### Python 3 — 586 bytes

```python
N=v=0;L=[];K=4308
for c in b"TT'S0m-[=%(`.PBr]eW{122|>E$0GdE=Nv,SpR4S9VwZhC\rMp>$j'd+Qu&!QFTyPhJOgloJl1!|f{vGi;yQQI]Ai Lu{xw!^'gaa9)qhk#c^ayrP	i^tw87uBJ/p~`)MH\\X.fq%5_YaQx+`O1qnASybEUgk:Oml{QQ^dmJO?bG\0{W#2$nO1I}y!AZTO5RK`kJ'Lh{\"@={43gKeDJk0TPNQ#h	}0d	z$3|EV\\U9Y/,\rw(>kigv!ZFsL'Dc#]8/<Q?G7~k#I`!w6_Lsi?/Z?ZQi\r)<Fv{mv}^ow:o'@":N=N*128+c
while N>1:
 while N%2:v+=K;N//=2
 v+=N//2%K;N//=2*K;x=1;y=v
 for p,r in zip(b'\r/',b'('):x*=p**(y%r);y//=r
 L+=x,
print(*sorted(L),sep='\n')
```

The literals hold raw ASCII control characters (and DEL), so the code block
above may look garbled; only bytes 0, 10, 13, the quote and the backslash are
escaped. Their contents are described below.

**How it works**

- **The data.** The sequence is finite: the degrees χ(1) of the 184
  irreducible complex characters of the Baby Monster group B (one for each conjugacy class), in
  increasing order and with repeats. They come from the character table of
  the Baby Monster group B in the ATLAS of Finite Groups (Conway, Curtis, Norton, Parker and
  Wilson, 1985), also in GAP's character table library (table "B"); the
  OEIS b-file by Eric M. Schmidt lists the same 184 numbers. The program
  stores them; nothing is computed from the group. The stored list passes
  two checks: Σ a(n)² = |B| = 4154781481226426191177580544000000 (the squares of the irreducible
  degrees of a finite group add up to its order), and every a(n) divides
  |B|.
- **Degrees as exponent vectors.** Every degree divides
  |B| = 2⁴¹·3¹³·5⁶·7²·11·13·17·19·23·31·47, so it is a product of powers of those 11 primes. Taking
  the primes in the order 13, 23, 47, 31, 3, 5, 19, 7, 2, 11, 17 (the second bytes literal) with radices
  2, 2, 2, 2, 14, 7, 2, 3, 40, 2, 2 (the third literal; the radix of p is 1 + the largest exponent
  of p among the degrees), the exponents are the digits of a mixed-radix
  number v, least significant first. `for p,r in zip(…):x*=p**(y%r);y//=r`
  turns v back into the degree.
- **Sorted codes, Rice-coded gaps.** The 184 codes v are sorted and stored
  as their gaps. A gap qK + s (K = 4308) is written as q one-bits, a zero
  bit, then s as one base-K digit, all read from the low end of a single
  integer N that has a 1 on top as an end mark. `while N%2:v+=K;N//=2` adds
  the qK, `v+=N//2%K;N//=2*K` drops the zero bit and adds s, and
  `while N>1` stops at the end mark.
- **The literal.** N is written in base 128, most significant digit first,
  as the first bytes literal (iterating over bytes gives ints), and
  `N=N*128+c` reads it back.
- **Output.** The degrees come out in code order; `sorted(L)` puts them in
  increasing order, they are printed one per line, and the program stops.

**Notes**

- Sizes: the decimal digits of the 184 terms are 2637 characters. The
  exponent vectors in mixed radix, kept in sequence order, take 561
  bytes; sorting them by code first frees their order (about log₂ 184! bits
  of the plain encoding), which the gap code turns into the shorter
  literal. The prime order and K came from a small search for the shortest
  literal.
- The program prints the 184 terms and stops, as a finite sequence should;
  it takes well under a second. The bar is all 184 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 586 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001378), CC BY-SA 4.0.
