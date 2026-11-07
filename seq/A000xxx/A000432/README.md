# A000432

> Series-parallel numbers.
> — [OEIS A000432](https://oeis.org/A000432)

Offset 3: 8, 52, 288, 1424, 6648, 29700, 128800, 545600, 2269672, 9303140, …

a(n) is the coefficient of x^(n−3) in 4(2 + S)(1 + S)/(1 − S)⁵ (Sean Irvine's
formula on the OEIS page), where S(x) = Σ_{k≥1} s(k)x^k is the generating
function of the series-parallel networks [A000084](../A000084/).

### Python 3 — 165 bytes

```python
A=[1,n:=1]
while 1:B=64**n;T=sum(A[k]*B**k for k in range(n));print(4*T*-~T*pow(2-T,-5,B**n)*B//B**n%B);n+=1;A+=sum(sum(A[-d::-d])*d*A[d]for d in(1,*range(1,n)))//n,
```

**How it works**

- A holds s(0) = 1 (an auxiliary value) and s(1), s(2), …; the last statement
  appends s(n) with the A000084 recurrence
  n·s(n) = Σ_{d<n} w_d·Σ_{j≥1} s(n − jd), w_1 = 2 and w_d = d·s(d) for
  d ≥ 2 (derived on that page): d = 1 is listed twice in `(1,*range(1,n))`,
  and `A[-d::-d]` walks back through s(n−d), s(n−2d), … down to s(0).
- The term printed in pass n is h_m, m = n − 1, the coefficient of x^m in
  H(x) = 4(2 + S)(1 + S)/(1 − S)⁵, which is a(m + 3). It is computed by
  evaluating the series at the integer B = 64ⁿ modulo Bⁿ: T = 1 + S(B)
  truncated to degree n − 1, so 4·T·(T + 1) = 4(1 + S)(2 + S) and 2 − T = 1 − S
  at x = B. `-~T` is T + 1.
- 1 − S(B) ≡ 1 (mod B), so it is invertible modulo Bⁿ, and
  `pow(2-T,-5,B**n)` agrees modulo Bⁿ with the truncated series of
  (1 − S)^(−5) evaluated at B. The product is then ≡ Σ_{j<n} h_j·B^j
  (mod Bⁿ), and `*B//B**n%B` (that is, ⌊·/B^(n−1)⌋ mod B) reads off the digit
  h_{n−1}, provided every h_j with j < n is below B.

**Why B = 64ⁿ is big enough**

- Every series-parallel network is the value of a plane binary expression
  tree with k leaves whose k − 1 internal nodes are labelled series or
  parallel, so s(k) ≤ 4^(k−1)·2^(k−1) < 8^k. Hence
  S(1/32) < Σ_{k≥1} 4^(−k) = 1/3.
- H has nonnegative coefficients and increases with S on [0, 1), so
  Σ_j h_j·32^(−j) = H(S(1/32)) ≤ H(1/3) = 189/2 < 128, and every
  h_j < 128·32^j. For j ≤ n − 1 that is at most 4·32ⁿ ≤ 64ⁿ when n ≥ 2; at
  n = 1 the only digit is h_0 = 8 < 64.

**Notes**

- B = 2^(5n+3) (`B=8<<5*n`) is also big enough and 1 byte longer. Packing
  only s(1), …, s(n−1) into S and writing `(2+S)*(1+S)` and `pow(1-S,…)`:
  173 bytes. The three statements on separate lines: 169.
- Exact integer arithmetic, and the digit bound above holds for every n, so
  the program is right for every n.
- Bⁿ has 6n² bits, so the modular inverse dominates: about 144 terms in 60 s
  here.
- The b-file has 38 terms (up to a(40)); the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 184 | first entry |
| 2026-11-07 | Python 3 | 165 | B = 64ⁿ, pack s(0) into T = 1 + S, one-line loop |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000432), CC BY-SA 4.0.
