# A001332

> a(n) = Bernoulli(2*n) * (2*n + 1)!.
> — [OEIS A001332](https://oeis.org/A001332)

Offset 0: 1, 1, −4, 120, −12096, 3024000, −1576143360, 1525620096000, …

a(n) = B₂ₙ·(2n+1)! is an integer: by the von Staudt–Clausen theorem the
denominator of B₂ₙ is the product of the primes p with p − 1 | 2n, all at
most 2n + 1, so it divides (2n+1)!.

### Python 3 — 98 bytes

```python
c=1;m=0
while 1:s=0;print(sum((c:=c*(j-m-2)//j)//j*(s:=s-j**m)for j in range(1,m+2)));m+=2;c*=m*~m
```

**How it works**

- Let N = 2n and M = N + 1. By Faulhaber's formula the power sum
  P(x) = 1ᴺ + 2ᴺ + … + xᴺ is a polynomial in x of degree M with no constant
  term, and its coefficient of x is B_N (for N = 0, P(x) = x). So
  q(x) = P(x)/x is a polynomial of degree N with q(0) = B_N.
- Lagrange interpolation of q through x = 1, …, M, evaluated at 0, has the
  weights ∏_{i≠j} i/(i−j) = (−1)^(j−1)·C(M, j). Multiplying by M! gives
  a(n) = Σ_{j=1}^{M} (−1)^(j−1)·C(M, j)·(M!/j)·P(j), a sum of integers.
- In the code m = N. `c` runs through c_j = (−1)^j·C(M, j)·M! by
  c_j = c_{j−1}·(j − 1 − M)/j, which is `c*(j-m-2)//j`; the division is
  exact because c_{j−1}·(j − 1 − M) = j·c_j. `c//j` is exact too, since
  j ≤ M divides M!. `s:=s-j**m` keeps s = −P(j), so each product is
  (−1)^(j−1)·C(M, j)·(M!/j)·P(j), and `range(1,m+2)` is j = 1, …, M.
- `c` carries over from term to term: the sum starts from c_0 = M! and
  leaves c = c_M = (−1)^M·M! = −M!, as M is odd. After `m+=2`,
  `c*=m*~m` multiplies by −(M+1)(M+2), which gives (M+2)!, the next
  c_0. It starts at 1 = 1! for m = 0, and `s=0` resets the power sum.
- Exact integer arithmetic throughout, so every term is right.

**Notes**

- Counting by M = 2n + 1 instead (`c=m=1`, `(j+~m)`, `j**~-m`,
  `range(1,m+1)`, `c*=m-m*m`) is also 98 bytes; keeping M! in a separate
  `f` and setting `c=-f` before each term is 103; `while[s:=0,print(…)]:`
  ties with `while 1:s=0;`.
- The explicit double sum B_N = Σ_k 1/(k+1)·Σ_j (−1)^j·C(k, j)·jᴺ, scaled
  by (N+1)! and written like [A000146](../../A000xxx/A000146/), is 115
  bytes (with a separate `print(1)` for a(0)); with `math.comb` it is 128.
  The tangent-number boustrophedon of [A000367](../../A000xxx/A000367/)
  needs the extra factor 2n·(2n+1)!/(4ⁿ(4ⁿ−1)) and a sign, and came out
  longer in drafts.
- Python's 4300-digit int-to-str limit stops the program at a(497), the
  first term with more than 4300 digits, after printing a(0) to a(496)
  (about 20 s).
- The b-file has 51 terms (n = 0 to 50); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001332), CC BY-SA 4.0.
