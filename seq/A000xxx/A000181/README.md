# A000181

> a(n) = A058087(n,n-4).
> — [OEIS A000181](https://oeis.org/A000181)

Offset 4: 2, 15, 60, 469, 3660, 32958, 328920, 3614490, 43341822, 563144725, …

### Python 3 — 113 bytes

```python
from math import*
n=4
while[print(n*sum((-1)**j*comb(j,3)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//-2)]:n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t⁴. It
  counts the permutations π of 1..n with exactly four i such that
  π(i) ≡ i or i+1 (mod n).
- The coefficient of t⁴ in (t−1)^k is (−1)^k·C(k,4), so
  a(n) = Σ_k (−1)^k·C(k,4)·(2n/(2n−k))·C(2n−k,k)·(n−k)!.
- Two identities shrink the summand, as in [A000159](../A000159/): C(m,k)/m =
  C(m−1,k−1)/k with m = 2n−k, then C(k,4)/k = C(k−1,3)/4. The k = 0 term
  is 0 anyway. With j = k−1 this gives
  a(n) = −(n/2)·Σ_{j=0..n−1} (−1)^j·C(j,3)·C(2n−2−j,j)·(n−1−j)!.
- For four hits `comb(j,3)` (9 bytes) beats the falling factorial
  `j*~-j*(j-2)` (11 bytes, plus `//-12` instead of `//-2`), the reverse of
  A000159, where `j*~-j` was shorter than `comb(j,2)`.
- The minus sign goes into the divisor: n times the sum is exactly −2·a(n),
  so `//-2` is exact. It is cheaper than `(-1)**-~j` in every term.
- `perm(x)` with one argument is x!, four bytes under `factorial(x)`;
  `n+~j` is n−1−j. The terms j = 0, 1, 2 vanish.

**Notes**

- Each term is a sum of n exact big-integer products, correct for every n.
  The whole b-file (247 terms) prints in about a second and about 1270
  terms come out in 60 s on a home PC. The bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits); a(1559) has 4302.
- Checked against shorter ideas: a big-base digit extraction of U_n
  (+15 bytes), brute force over permutations (longer and far slower), and a
  search for a short recurrence in n for U_n(t) itself (none of order ≤ 3
  with coefficients of degree ≤ 2 in n and t).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000181), CC BY-SA 4.0.
