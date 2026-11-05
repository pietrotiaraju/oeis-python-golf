# A000159

> a(n) = A058087(n,n-3).
> — [OEIS A000159](https://oeis.org/A000159)

Offset 3: 2, 8, 20, 152, 994, 7888, 70152, 695760, 7603266, 90758872, …

### Python 3 — 108 bytes

```python
from math import*
n=3
while[print(n*sum((-1)**j*j*~-j*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//3)]:n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t³. It
  counts the permutations π of 1..n with exactly three i such that
  π(i) ≡ i or i+1 (mod n).
- The coefficient of t³ in (t−1)^k is (−1)^(k−3)·C(k,3), so
  a(n) = Σ_k (−1)^(k−3)·C(k,3)·(2n/(2n−k))·C(2n−k,k)·(n−k)!.
- Two identities shrink the summand: C(m,k)/m = C(m−1,k−1)/k with
  m = 2n−k, then C(k,3)/k = C(k−1,2)/3. The k = 0 term is 0 anyway
  (C(0,3) = 0). With j = k−1 this gives
  a(n) = (n/3)·Σ_{j=0..n−1} (−1)^j·j(j−1)·C(2n−2−j,j)·(n−1−j)!.
- `perm(x)` with one argument is x!, four bytes under `factorial(x)`;
  `~-j` is j−1 and `n+~j` is n−1−j. The terms j = 0 and 1 vanish.
- a(n) is an integer, so n times the sum is a multiple of 3 and `//3` is
  exact.

**Notes**

- Each term is a sum of n exact big-integer products. The whole b-file
  (248 terms) prints in about a second and about 1150 terms come out in
  60 s. The bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4299 digits); a(1559) has 4302.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 108 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000159), CC BY-SA 4.0.
