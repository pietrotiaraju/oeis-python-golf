# A000264

> Number of 3-edge-connected rooted cubic maps with 2n nodes and a distinguished Hamiltonian cycle.
> — [OEIS A000264](https://oeis.org/A000264)

Offset 1: 1, 1, 3, 14, 80, 518, 3647, 27274, 213480, 1731652, 14455408, 123552488, 1077096124, 9548805240, 85884971043, 782242251522, …

### Python 3 — 132 bytes

```python
n=0
while 1:n+=1;M=27**n;t=1;print((M-pow(1+sum((t:=t*M*(16*j*j-4)//-~j//(j+2))for j in range(1,n+1)),1-2*n,M**-~n)//M**n)//(4*n-2))
```

**How it works**

- The OEIS page gives the functional equation (Sean A. Irvine)
  B(x) = A(x·(1+2B(x))²), where A is this sequence and
  b(n) = C(n)·C(n+1)/2 is a product of Catalan numbers. Put
  G(x) = 1 + 2B(x) = Σ_{j≥0} C(j)·C(j+1)·x^j = 1 + 2x + 10x² + 70x³ + …
  and y = x·G(x)². The equation says G(x) = 1 + 2A(y).
- Lagrange inversion of y = x·G(x)² gives
  [y^n] A = (1/2n)·[x^(n−1)] G′(x)·G(x)^(−2n), and since
  G′·G^(−2n) is the derivative of G^(1−2n)/(1−2n), this is
  a(n) = −[x^n] G(x)^(1−2n) / (4n−2).
- Kronecker substitution turns that power series into one integer. With
  M = 27^n, `g` = Σ_{j≤n} G_j·M^j is G truncated and evaluated at x = M.
  Because G_0 = 1, g ≡ 1 (mod M), so g is invertible modulo M^(n+1),
  and `pow(g,1-2*n,M**-~n)` (negative exponents work since Python 3.8)
  is P(M) mod M^(n+1), where P = Σ_{j≤n} c_j·x^j is G^(1−2n) truncated:
  g^(2n−1)·P(M) = 1 + M^(n+1)·(…).
- The c_j have mixed signs, and c_n = −(4n−2)·a(n) < 0. If every
  |c_j| < M, the residue is v = M^(n+1) + c_n·M^n + L with |L| < M^n,
  so v // M^n is M + c_n or M + c_n − 1, and M − v // M^n is |c_n| or
  |c_n| + 1. |c_n| is a multiple of 4n − 2 ≥ 2, so floor division by
  4n − 2 gives a(n) either way, with no rounding step.
- Why 27^n is big enough: G_j ~ 16^j/j³, so G converges absolutely on
  |x| = 1/16, and G(1/16) = 1.20939… (partial sum plus a tail below
  10⁻¹⁰). On the closed disc |x| ≤ 1/16 that gives
  |G(x)| ≥ 1 − (G(1/16) − 1) > 0.7906, and Cauchy's estimate gives
  |c_j| ≤ 16^j·0.7906^(1−2n) < 0.8·25.6^n < 27^n for j ≤ n.
  (In practice the largest |c_j| grows like about 9.4^n, so 9^n would
  fail.)
- `g` comes from the term ratio G_j/G_(j−1) = C(j+1)/C(j−1) =
  4(2j−1)(2j+1)/((j+1)(j+2)): the walrus `t` holds G_j·M^j, so each step
  multiplies by M·(16j²−4) and divides by j+1 and j+2. The divisions are
  exact, because two floor divisions in a row equal one floor division by
  the product.

**Notes**

- Correctness rests on the functional equation from the OEIS page, which
  reproduces all 200 b-file terms, and on the bound above. The arithmetic
  is exact integer arithmetic, so the program is right for every n.
- The modular inverse of a number of about 4.75·n² bits dominates the
  time, and CPython's inverse is quadratic, so the cost grows fast: on
  the test machine it printed about 155 terms in 60 s. The bar is 120 terms in
  60 s; the b-file has 200 (n = 1 to 200).
- Computing G^(1−2n) with the power-of-a-series recurrence
  k·P_k = Σ_j ((α+1)j − k)·G_j·P_(k−j), α = 1 − 2n, prints the whole
  b-file in a few seconds but is about 30 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 132 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000264), CC BY-SA 4.0.
