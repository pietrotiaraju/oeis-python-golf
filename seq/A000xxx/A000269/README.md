# A000269

> Number of trees with n nodes, 3 of which are labeled.
> — [OEIS A000269](https://oeis.org/A000269)

Offset 3: 3, 16, 67, 251, 888, 3023, 10038, 32722, 105228, 334836, 1056611, 3311784, …

### Python 3 — 147 bytes

```python
*r,n=1,1,2
while 1:r+=sum(-~j*r[j]*sum(r[~j::~j])for j in range(n))//n,;n+=1;X=8**n;T=0;[T:=T*X+c for c in r];print(T**3*(T+3*(U:=X**n-T))//U**3%X)
```

**How it works**

- Take the smallest subtree that holds the three labeled nodes. Either it
  is a path with one labeled node inside (3 choices for that node, and the
  path is a sequence of at least three rooted trees), or it is a tripod
  around an unlabeled centre (the centre's rooted tree times three nonempty
  sequences of rooted trees, one per branch). With B the g.f. of rooted
  trees ([A000081](../A000081/)) this gives
  3B³/(1−B)² + B⁴/(1−B)³ = B³(3−2B)/(1−B)³, Jovovic's formula. With
  P = B/(1−B) the same thing is **A = B·P²·(P+3)**.
- `r` holds b(1), …, b(n), oldest first, grown by the Euler-transform
  recurrence **n·b(n+1) = Σ_{e=1..n} e·b(e)·Σ_{j≥1} b(n+1−je)** exactly as
  in [A000243](../A000243/). The start `*r,n=1,1,2` runs it once before the
  first print, so the output begins at a(3).
- Instead of series products, the program evaluates everything at the
  single point x = 1/X with X = 8ⁿ. Horner over `r` gives
  **T = Σ_{i≤n} b(i)·X^(n−i)**, so B_n(1/X) = T/Y with Y = Xⁿ, where B_n is B
  cut at degree n. With U = Y − T, P(1/X) = T/U and
  Y·A_n(1/X) = T·(T/U)²·(T/U + 3) = **T³(T+3U)/U³**.
- Here A_n = B_n³(3−2B_n)/(1−B_n)³ agrees with A up to xⁿ, so
  Y·A_n(1/X) = Σ_{i≤n} a(i)·X^(n−i) + τ, where τ = Σ_{j≥1} a′(n+j)·X^(−j)
  collects the higher coefficients of A_n. The floor division drops τ and
  `%X` keeps the last digit, a(n).

**Notes**

- Why the digits don't overlap: all the series involved have nonnegative
  coefficients (A is Σ_{k≥3} (k−2)(k+3)/2·Bᵏ), so a′(k) ≤ a(k) and
  a(k) ≤ A(1/4)·4ᵏ. Summing the tree counts gives B(1/4) = 0.38079…
  (the tail past b(400) is under (3/4)⁴⁰⁰ since b(k)·ρᵏ ≤ B(ρ) = 1), so
  A(1/4) = 0.5206… and a(k) < 4ᵏ. Hence every a(i) with i ≤ n is below
  4ⁿ < X, and τ < Σ_{j≥1} 4^(n+j)/8^(nj) < 4·2^(−n) + 0.004 ≤ 0.51 for
  n ≥ 3.
  Everything else is exact integer arithmetic, so the program is right for
  every n.
- T has 3n² bits, so each term costs a Horner pass and a few products of
  that size. The whole b-file (198 terms, n up to 200) prints in about
  15 s here and about 300 terms come out in 60 s; the bar is the whole
  b-file in 60 s.
- Multiplying the series directly, with the L = 1/(1−B) list of
  [A000243](../A000243/) and its square and cube, needs three dot products
  and is much longer. The same evaluation in the forward direction,
  B(X) mod X^(n+1) with `pow(1-Q,-3,M)`, is longer than the floor
  division too.
- The `while[…]:` header form (Horner and print in the loop condition,
  recurrence in the body) needs `T:=0,` and a 4-term start
  `*r,n=1,1,2,3`, 3 bytes more. Inlining `8**n` instead of naming X costs
  2 bytes; Horner on U (start 1, subtract each b) instead of T comes out
  the same length.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000269), CC BY-SA 4.0.
