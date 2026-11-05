# A000214

> Number of equivalence classes of Boolean functions of n variables under action of AG(n,2).
> — [OEIS A000214](https://oeis.org/A000214)

Offset 1: 3, 5, 10, 32, 382, 15768919, 16224999167506438730294, …

### Python 3 — 197 bytes

```python
n=r=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^~i%N for y in m];t+=r;r=len({*m})>>n;k+=r
  for x in m:
   while~x:m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**What is counted**

The affine group AG(n,2) is the set of maps g(x) = A·x ⊕ b with A an invertible
n×n matrix over GF(2). It acts on the N = 2ⁿ inputs, so it acts on the 2^N
Boolean functions. By Burnside's lemma,

a(n) = (1/|AG(n,2)|) · Σ_g 2^c(g),

where c(g) is the number of cycles of g on the N points: a function is fixed by
g exactly when it is constant on each cycle.

**How it works**

- **Every affine map.** i runs over 2^(n²+n) = N^(n+1) values. Its lowest base-N
  digit is b and the next n digits give the columns of A (complemented, see
  below). The list starts as `[b]`, and each column c doubles it with
  `m+=[y^c for y in m]`, so in the end m[x] = b ⊕ Σ x_j·c_j = g(x). The walrus
  in `[m:=[i%N]]*n` resets m and gives the n passes of the doubling loop in one
  go.
- **Only bijections.** `r=len({*m})>>n` is 1 when the N values of m are
  distinct and 0 otherwise, so singular A count for nothing. Before the last
  doubling m has fewer than N entries and r is 0 too, so `k+=r` counts each
  bijection once and k ends at |AG(n,2)| = 2ⁿ·|GL(n,2)|.
- **Cycles.** `for x in m` reads each position in turn. If that position was
  already visited it reads −1 and skips; otherwise it reads a point of an
  unvisited cycle and walks it, marking every point −1. The step that lands on
  a marked point sets x to −1, ends the walk and doubles r, so r ends at
  2^c(g) (or 0).
- **Adding r one map late.** `t+=r` sits in the doubling loop: on the first
  pass it adds the previous map's r, and on the other passes r is still 0.
  The columns are read as `~i%N` instead of `i%N` so that the last value of i
  has every column 0: that map is singular, its r is 0, and nothing is lost at
  the end of a row or carried into the next one. The very first pass adds the
  initial r = 1, so n = 1 ends with t = 7 = 3·2 + 1, and `t//k` drops it
  because k = 2.

**Speed**

The loop visits all 2^(n²+n) choices of (A, b): a(4) takes about 17 s here,
and a(5) would need 2³⁰ maps, many hours. The bar is the first 4 terms within
60 s.

**Notes**

- The same program with `itertools.product` (`for b,*p in
  product(*[range(2**n)]*-~n):`, `m=[b]`, and `t+=r;k+=r>0` after the walk)
  is 226 bytes: reading the digits off one integer saves the import and the
  unpacking.
- The cycle walk of [A000157](../A000157/) tests `~m[x]` and shifts on
  `m[x]<0`; testing x itself, which becomes −1 exactly when the cycle closes,
  is 6 bytes shorter.
- Without the complement the last map for n = 1 is a bijection (r = 2). The
  result is still right with an initial r of 2 or 3, but `n=1;r=2` costs a
  byte more than `n=r=1` plus `~`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 197 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000214), CC BY-SA 4.0.
