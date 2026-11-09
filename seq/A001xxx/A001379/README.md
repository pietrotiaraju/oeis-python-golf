# A001379

> Degrees of irreducible representations of Monster group M.
> — [OEIS A001379](https://oeis.org/A001379)

Offset 1: 1, 196883, 21296876, 842609326, 18538750076, 19360062527, 293553734298, 3879214937598, …

### Python 3 — 848 bytes

```python
N=v=0;L=[];K=1356223
for c in b"0\0HryMRE'Q,&gpE`nppE`:u0@s,)[8/9U.0rAS!l,0-Hab%?^rx2hFaNEEWCO i%V>*J?ip%)ItA	p+lJ%?iKfVOwV%Fa))j5#cRRmPeF}ih9lak \rXdH3{:5nua(=0cp:u9[7pC+dpHqi=frt8&d?q6!Zkprp NhG/*F`N3nPF;Y$\\7-t'O24oT_J}AKhTw\nhbV0g[`2<3q<!R~+z&~>[S(bpMI3[9Ur5S{V-\\-gjELsnP3+5l'WsO|ji!.&@Xgo2&2k\0@/T.9!lGgs%>cAP({kg0.:H~p]q XU4nr$'W\\4sToL#)2m,_[w-O3ernNlBlAg@e#T5p$AMUR%8\nQi@Qp^;TVoyA~V=G*N;Vi/2SgO5Rj^RH'W\0f`{3A_(Uk-,_D`xsOx-[mb}_l;^r-pTr_[~TS>A'$'<BZW]Ve(r-,m\rWT(]4K^zK|dAF#9rc/zqCYKQX@r:;N2x:Bg@L@jonxXE$yM@'h,l^^vzo>7(zDIov[ ":N=N*128+c
while N>1:
 while N%2:v+=K;N//=2
 v+=N//2%K;N//=2*K;x=1;y=v
 for p,r in zip(b';)/G\r',b'\n/'):x*=p**(y%r);y//=r
 L+=x,
print(*sorted(L),sep='\n')
```

The literals hold raw ASCII control characters (and DEL), so the code block
above may look garbled; only bytes 0, 10, 13, the quote and the backslash are
escaped. Their contents are described below.

**How it works**

- **The data.** The sequence is finite: the degrees χ(1) of the 194
  irreducible complex characters of the Monster group M (one for each conjugacy class), in
  increasing order and with repeats. They come from the character table of
  the Monster group M in the ATLAS of Finite Groups (Conway, Curtis, Norton, Parker and
  Wilson, 1985), also in GAP's character table library (table "M"); the
  OEIS b-file by Eric M. Schmidt lists the same 194 numbers. The program
  stores them; nothing is computed from the group. The stored list passes
  two checks: Σ a(n)² = |M| = 808017424794512875886459904961710757005754368000000000 (the squares of the irreducible
  degrees of a finite group add up to its order), and every a(n) divides
  |M|.
- **Degrees as exponent vectors.** Every degree divides
  |M| = 2⁴⁶·3²⁰·5⁹·7⁶·11²·13³·17·19·23·29·31·41·47·59·71, so it is a product of powers of those 15 primes. Taking
  the primes in the order 59, 41, 29, 17, 47, 23, 5, 71, 2, 3, 13, 19, 31, 11, 7 (the second bytes literal) with radices
  2, 2, 2, 2, 2, 2, 10, 2, 47, 21, 4, 2, 2, 3, 7 (the third literal; the radix of p is 1 + the largest exponent
  of p among the degrees), the exponents are the digits of a mixed-radix
  number v, least significant first. `for p,r in zip(…):x*=p**(y%r);y//=r`
  turns v back into the degree.
- **Sorted codes, Rice-coded gaps.** The 194 codes v are sorted and stored
  as their gaps. A gap qK + s (K = 1356223) is written as q one-bits, a zero
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

- Sizes: the decimal digits of the 194 terms are 4447 characters. The
  exponent vectors in mixed radix, kept in sequence order, take 831
  bytes; sorting them by code first frees their order (about log₂ 194! bits
  of the plain encoding), which the gap code turns into the shorter
  literal. The prime order and K came from a small search for the shortest
  literal.
- The program prints the 194 terms and stops, as a finite sequence should;
  it takes well under a second. The bar is all 194 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 848 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001379), CC BY-SA 4.0.
