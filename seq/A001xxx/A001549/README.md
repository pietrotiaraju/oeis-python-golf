# A001549

> Related to Gilbreath conjecture.
> — [OEIS A001549](https://oeis.org/A001549)

Offset 1: 4, 10, 17, 18, 30, 34, 69, 109, 111, 189, 192, 193, 194, 195, 311, 763, …

**Definition (reconstructed).** The entry gives no formula beyond its
title; it comes from Killgrove and Ralston's check of Gilbreath's
conjecture (Math. Comp. 13 (1959)). R. J. Mathar's comment on the entry
describes the terms as the records of n + A000232(n), and this page
follows that:

- Gilbreath's triangle: row 0 is the primes p₀ = 2, p₁ = 3, p₂ = 5, …;
  row r + 1 holds the absolute differences of neighbours in row r. For
  r ≥ 1 let c(r) be the 0-based column of the first entry > 2 in row r
  (that is A000232(r)), and m(r) = r + c(r): that entry is computed from
  p_c(r), …, p_m(r), so m(r) is the index of the last prime it needs.
- In row r every entry left of c(r) is 0, 1 or 2, so every entry of
  row r + 1 left of c(r) − 1 is too: c(r+1) ≥ c(r) − 1, i.e.
  m(r+1) ≥ m(r). The records of m are therefore its distinct values in
  increasing order, and that is the sequence: 4, 10, 17, 18, 30, 30, 30,
  30, 34, … gives 4, 10, 17, 18, 30, 34, ….
- This reading matches **all 83 terms** of the b-file (up to
  98091489): a separate check (numpy, not part of the record) built the
  triangle over all 98842358 primes below 2013265920 (rows 1–400), and
  its distinct m values up to 98091489 are exactly the b-file. Rows
  1–274 finish within those primes and row 275 does not, so the next
  term is beyond 98842357.

### Python 3 — 201 bytes

```python
N=m=1
while s:=[1]*(N:=2*N):
 L=[];r=1
 for i in range(2,N):s[i*i::i]=[0]*(-i--N//i);L+=[i]*s[i]
 while~(i:=bytes(map(2 .__lt__,L:=[abs(x-y)for x,y in zip(L,L[1:])])).find(1)):r+i>m!=print(m:=r+i);r+=1
```

**How it works**

- Passes with N = 2, 4, 8, …. Each starts with a sieve of Eratosthenes
  on 0 … N − 1: for every i ≥ 2, `s[i*i::i]=[0]*(-i--N//i)` clears the
  multiples of i from i² on (−i − (−N//i) = ⌈N/i⌉ − i is that slice's
  length, ≤ 0 once i² ≥ N, so the slice and the list are both empty).
  When the loop reaches i, all smaller factors are done, so s[i] is
  final and `L+=[i]*s[i]` collects the primes below N in order.
- `L:=[abs(x-y)for x,y in zip(L,L[1:])]` turns row r − 1 into row r
  (r counts the rows), and `bytes(map((2).__lt__,L)).find(1)` is the
  first column i whose entry is > 2, or −1.
- Every computed entry is exact: it only uses primes below N. So a
  found i is c(r) and r + i = m(r). If row r has no entry > 2 among its
  computed columns, m(r) needs more primes and so does every later row
  (m only grows): `~i` is 0, the pass ends, and the next one doubles N
  and starts over. `r+i>m!=print(m:=r+i)` prints only values beyond the
  last printed one, so each term comes once and in order.
- Nothing assumes that every row has an entry > 2 (that is not known):
  if one never did, the sequence would end there and the program would
  keep doubling without printing anything wrong.

**Notes**

- Exact integer arithmetic. A pass costs about N list entries of memory
  (8 bytes each) plus the prime list, and a sieve plus about (number of
  rows) × π(N) differences.
- The b-file has 83 terms; the bar is 44 terms in 60 s. Terms 43 and 44
  (271743, 271747) end the pass with N = 2²² after about 23 s here
  (about 17 reference seconds); the pass with N = 2²³ brings terms 45–50
  (up to 516042) at about 48 s, and N = 2²⁴ needs about 140 MB for the
  sieve list.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 201 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001549), CC BY-SA 4.0.
