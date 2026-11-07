# A000412

> Number of bipartite partitions of n white objects and 3 black ones.
> — [OEIS A000412](https://oeis.org/A000412)

Offset 0: 3, 7, 16, 31, 57, 97, 162, 257, 401, 608, …

This is a multiset partition of n identical white objects and 3
identical black ones. A fixed black total reduces the two-variable
product to the ordinary partition series and a fixed collection of
rational filters, combined directly without a polynomial convolution.

a(n) is the number of ways to write the vector (n, 3) as an unordered sum
of nonzero vectors (i, j) with nonnegative integer entries: i white and j
black objects per part. For example a(0) = 3, from (0,3), (0,2) + (0,1)
and (0,1) + (0,1) + (0,1).

### Python 3 — 149 bytes

```python
*a,n=1,0;S=[];M=int.__mul__
while[print(sum(map(M,(3,1,-1,-2,-1,1),a)))]:n+=1;S+=sum(d<<(d<4)for d in range(1,n+1)if n%d<1),;a=[sum(map(M,S,a))//n]+a
```

**How it works**

- The generating function is [y³] Π_{(i,j)≠(0,0)} 1/(1 − xⁱyʲ). The parts
  with j = 0 give P(x) = Π_{i≥1} 1/(1 − xⁱ). For each j ≥ 1, Euler's
  identity Π_{i≥0} 1/(1 − z·xⁱ) = Σ_m z^m/D_m(x), with z = yʲ and
  D_m(x) = (1 − x)(1 − x²)…(1 − x^m), turns m parts of black size j into a
  factor 1/D_m. The black partitions 3, 2 + 1 and 1 + 1 + 1 of 3 therefore
  give

  Σ a(n)xⁿ = P·(1/D₁ + 1/D₁² + 1/D₃) = H·(3 + x − x² − 2x³ − x⁴ + x⁵),

  with H = P/D₃: the polynomial is (1 − x²)(1 − x³) + (1 + x)(1 − x³) + 1.
- H counts partitions in which the parts 1, 2, 3 come in two kinds, so
  H = Π_k (1 − x^k)^(−w(k)) with w(k) = 2 for k ≤ 3 and 1 otherwise. Its
  logarithmic derivative gives, for m ≥ 1,

  m·h(m) = Σ_{k=1}^{m} c(k)·h(m − k),  c(k) = Σ_{d | k} d·w(d).

- With n = m, `d<<(d<4)` is d·w(d), so the new entry of `S` is c(m).
- `S` = [c(1), …, c(m)] and `a` = [h(m−1), …, h(0)] (new values are put in
  front), so `sum(map(M,S,a))` is m·h(m) and `//n` is an exact division.
  `M=int.__mul__` names the multiplication used by both `map` calls.
- The header prints Σ qᵢ·h(m − i) for the coefficients
  `(3,1,-1,-2,-1,1)` of the polynomial: `map` stops at the shorter
  argument, which drops exactly the terms h(m − i) with m − i < 0.

**Notes**

- The slice form of the same recurrence,
  `*a,n=1,0` / `while[print(sum(map(int.__mul__,(3,1,-1,-2,-1,1),a[::-1])))]:n-=1;a+=sum(sum(a[d::d])*d<<(d>-4)for d in range(n,0))//n,`,
  is 128 bytes, but it adds about m·ln m slice entries per term instead
  of m products and prints only about 8600 terms in 60 s here, short of
  the bar (the previous 152-byte program, built the same way, about 8100).
  With n = −m, `range(n,0)`, `n%d>-1` (for d < 0, `n%d` lies in (d, 0])
  and `d<<(d>-4)` the program is also 149 bytes.
- Exact integer arithmetic and exact divisions, so the program is right
  for every n.
- The whole b-file (10001 terms) prints in about 32 s here.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file
  in 60 s.
- a(10000) has 112 digits and a(n) has roughly 1.1·√n digits, so the
  4300-digit limit only comes near n = 1.5·10⁷, far beyond this O(n²)
  scan.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 275 | first entry |
| 2026-11-06 | Python 3 | 261 | use sumprod on padded coefficient history and combine queue updates |
| 2026-11-06 | Python 3 | 152 | sum the black-partition cases directly and use the divisor recurrence |
| 2026-11-07 | Python 3 | 149 | H = P/D₃ by divisor-sum convolution, times a degree-5 polynomial |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000412), CC BY-SA 4.0.
