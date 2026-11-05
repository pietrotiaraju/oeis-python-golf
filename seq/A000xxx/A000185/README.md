# A000185

> a(n) = A058087(n,n-5).
> — [OEIS A000185](https://oeis.org/A000185)

Offset 5: 2, 24, 140, 1232, 11268, 115056, 1284360, 15596208, 204710454, 2888897032, …

### Python 3 — 113 bytes

```python
from math import*
n=5
while[print(n*sum((-1)**j*perm(j,4)*comb(2*n-2-j,j)*perm(n+~j)for j in range(n))//60)]:n+=1
```

**How it works**

- Row n of A058087 lists the coefficients of the ménage hit polynomial
  U_n(t) = Σ_k (2n/(2n−k))·C(2n−k,k)·(n−k)!·(t−1)^k (Kaplansky and
  Riordan), highest power first, so a(n) is the coefficient of t⁵. It
  counts the permutations π of 1..n with exactly five i such that
  π(i) ≡ i or i+1 (mod n).
- The coefficient of t⁵ in (t−1)^k is (−1)^(k−5)·C(k,5), so
  a(n) = Σ_k (−1)^(k−5)·C(k,5)·(2n/(2n−k))·C(2n−k,k)·(n−k)!.
- Two identities shrink the summand: C(m,k)/m = C(m−1,k−1)/k with
  m = 2n−k, then C(k,5)/k = C(k−1,4)/5. With j = k−1 and
  C(j,4) = j(j−1)(j−2)(j−3)/24 this gives
  a(n) = (n/60)·Σ_{j=0..n−1} (−1)^j·j(j−1)(j−2)(j−3)·C(2n−2−j,j)·(n−1−j)!.
- `perm(j,4)` is the falling factorial j(j−1)(j−2)(j−3), which is 0 for
  j < 4, so `range(n)` needs no lower bound. Taking it instead of
  `comb(j,4)` turns `2*n*…//5` into `n*…//60`, one byte shorter.
  `perm(x)` with one argument is x!, and `n+~j` is n−1−j.
- a(n) is an integer, so n times the sum is a multiple of 60 and `//60`
  is exact.

**Notes**

- Each term is a sum of n exact big-integer products. The whole b-file
  (246 terms) prints in about a quarter of a second and about 1170 terms
  come out in 60 s. The bar is the whole b-file in 60 s.
- Python's 4300-digit limit for printing ints stops the program after
  a(1558) (4298 digits); a(1559) has 4302.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 113 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000185), CC BY-SA 4.0.
