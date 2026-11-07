# A000510

> Maximal number of points in PG(2,q) with at most 3 on a line (next term is 21 or 22).
> — [OEIS A000510](https://oeis.org/A000510)

Offset 2: 7, 9, 9, 11, 15, 15, 17, …

a(i) is the largest size of a (k,3)-arc, a set of points of the projective
plane PG(2,q) with at most 3 on any line, where q runs through the prime
powers 2, 3, 4, 5, 7, 8, 9, … (a(2) is q = 2).

### Python 3 — 367 bytes

```python
q=1
while 1:
 q+=1;p=h=2
 while q%p:p+=1
 if p**q%q<1:
  Q=q**3;R=range(N:=q*q+q+1);A=lambda a,b,c=1:a+b and(a+c*b)%p+p*A(a//p,b//p,c)
  while len({*(G:=[t:=1]+[t:=A(t*p%Q,h,t*p//Q)for _ in[0]*Q*Q])})<Q-1:h+=1
  L=[sum(1<<(i+j)%N for i in R if A(A(G[i],G[i*q]),G[i*q*q])<1)for j in R]
  print(max(S.bit_count()*all((S&l).bit_count()<4for l in L)for S in range(1<<N)))
```

**How it works**

- The plane is built as in [A000509](../A000509/), which has the proofs.
  `p**q%q<1` keeps the prime powers q = pᵉ (p the smallest prime factor).
  GF(q³) is GF(p)[X]/(X^(3e) − h) for the first h ≥ 2 whose powers of X
  take Q − 1 = q³ − 1 distinct values, which makes X =: γ primitive;
  elements are integers read as base-p digit vectors, and `A(a,b,c)` adds
  c·b to a digit by digit mod p.
- `G[i]` is γ^i. The point classes γ^i·GF(q)*, 0 ≤ i < N = q² + q + 1, are
  the points of PG(2,q), D = {i : γ^i + γ^(iq) + γ^(iq²) = 0} (trace zero)
  is a line, and its N translates mod N are all the lines (Singer's cyclic
  model). `L` holds them as N-bit masks.
- The answer is a plain maximum over all 2^N point sets S: a set counts with
  its size `S.bit_count()` when every line meets it in at most 3 points,
  and with 0 otherwise (`*all(…)`).
- q = 2 is the Fano plane, whose lines all have 3 points, so all 7 points
  qualify and the first term is 7.

**Notes**

- The previous 781-byte version built GF(q) with affine coordinates and
  ran a branch-and-bound search that drops the points of every line that
  already holds three chosen points; it printed 4 terms (up to q = 5) in
  about 4 s here.
- Exhaustive and exact for every q; it rests only on Singer's construction
  of PG(2,q) and stores no values.
- The search has 2^N steps: 3 terms in about 10 s here (q = 4, N = 21,
  takes 9 s), but q = 5 needs 2³¹ sets and does not finish in practice.
- The b-file has 7 terms (up to a(8), q = 9); the bar is 3 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 1314 | first entry |
| 2026-11-06 | Python 3 | 794 | primitive-polynomial field arithmetic and direct affine line masks |
| 2026-11-06 | Python 3 | 781 | sum disjoint incident-line masks after removing the shared point |
| 2026-11-07 | Python 3 | 367 | Singer cyclic plane from GF(q³), brute force over all point sets |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000510), CC BY-SA 4.0.
