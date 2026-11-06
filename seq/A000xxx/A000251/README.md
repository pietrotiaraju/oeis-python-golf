# A000251

> Number of trees of diameter 6.
> — [OEIS A000251](https://oeis.org/A000251)

Offset 7: 1, 3, 11, 29, 74, 167, 367, 755, 1515, 2931, 5551, 10263, 18677, 33409, 59024, 102984, …

### Python 3 — 127 bytes

```python
n=7
while n:=n+1:
 P=S=b=B=4**n;M=B**n
 while b<M:S*=pow(q:=pow(1-b,-1,M),P//b%B,M);P*=q;b*=B
 print((S-P*(P-M//~-B+2))*B//M%B)
```

**What is counted**

- Let s_h(x) count rooted trees of height at most h by number of nodes, and
  r_h = s_h − s_(h−1) those of height exactly h. A height-≤h tree is a root
  with a multiset of height-≤(h−1) subtrees, so s_h = x·∏_j (1 − x^j)^(−c_j)
  with c_j the coefficient of x^j in s_(h−1). That gives s1 = x/(1 − x),
  s2 = x·∏_j 1/(1 − x^j) = Σ p(n−1)·x^n (p = partition numbers) and
  s3 = x·∏_j (1 − x^j)^(−p(j−1)).
- A tree of diameter 6 has one centre c, and rooted at c it has height 3 with
  at least two children of c carrying subtrees of height exactly 2; every such
  rooted tree is a diameter-6 tree with centre c. The rooted trees of height
  exactly 3 where c has only one height-2 child are counted by r2·s2 (that
  child's subtree, and the rest, rooted at c, of height ≤ 2). So the generating
  function is r3 − r2·s2 = s3 − s2·(1 − s1 + s2), the formula of Christian
  Sievers's PARI program on the OEIS page.

**How it works**

- A power series cut below x^n is stored as the integer Σ c_i·B^i with
  B = 4^n and M = B^n, so multiplying series is multiplying integers.
- `pow(1-b,-1,M)` with b = B^j is 1/(1 − x^j): the inverse of 1 − B^j modulo
  B^n is Σ_(jk<n) B^(jk). It exists because 1 − b is odd and M is a power of 2.
  `pow(q,d,M)` raises it to the d-th power by repeated squaring, so the huge
  exponents p(j − 1) cost only log d multiplications each.
- One loop builds s2 (`P`) and s3 (`S`): both start at B, which is the factor
  x, and step j multiplies `P` by 1/(1 − x^j) and `S` by (1 − x^j)^(−p(j−1)).
  The exponent is digit j of `P`, already final at that point since
  x/(1 − x^k) for k ≥ j only reaches degree j + 1 and up.
- `M//~-B` is 1 + B + … + B^(n−1), that is 1 + s1 below degree n, so
  `P-M//~-B+2` is 1 − s1 + s2. Digit n − 1 of the result, `*B//M%B`, is
  a(n − 1); n starts at 8 so the first line is a(7).

**Why the digits are exact**

- Every coefficient that appears below degree n is at most a coefficient of
  s3 at some degree ≤ n: that covers the binomials C(d + k − 1, k) of each
  factor, the partition numbers in `P` and the answer. A rooted tree with
  m nodes comes from at least one plane tree, and there are
  Catalan(m − 1) < 4^(m−1) plane trees, so all of them are below B = 4^n.
  Reducing modulo M is then exactly cutting the series, and reading a digit
  reads a coefficient.
- `S` and `P` are never reduced after `*=` (6 bytes shorter than `%M` on
  both): their digits from degree n up grow and carry, but only upwards, so
  the low n digits stay exact. The final combination may be negative because
  of those high digits; it is still L + B^n·H with 0 ≤ L < B^n holding the
  true coefficients, and Python's floor division picks digit n − 1 out of L.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Everything is recomputed for each n, and the unreduced `S` and `P` reach
  about 2n³ bits: 88 terms in 60 s here. The bar is 70 terms in 60 s; the
  b-file has 9280. Reducing both modulo M (`S=S*…%M`, `P=P*q%M`, 133 bytes)
  prints 93 terms in 30 s instead of 78.
- a(n) grows slower than any exponential (s3 has radius of convergence 1):
  a(9286), the last b-file term, has 1000 digits, so Python's 4300-digit
  int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 127 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000251), CC BY-SA 4.0.
