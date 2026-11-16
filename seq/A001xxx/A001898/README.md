# A001898

> Denominators of Bernoulli polynomials B(n)(x).
> — [OEIS A001898](https://oeis.org/A001898)

Offset 0: 1, 2, 12, 8, 240, 96, 4032, 1152, 34560, 7680, 101376, 18432, 50319360, …

### Python 3 — 222 bytes

```python
from fractions import*
from math import*
B=[[0,1]]
while[print(lcm(*[c.denominator for c in B[-1]]))]:m=len(B);B+=[m]+[sum(comb(m+1,i)*(i*sum(P[j:j+1])+(m-i)*sum(P[j-1:j]))for i,*P in B)/Fraction(m*~m)for j in range(m+1)],
```

**How it works**

- These are the Nörlund polynomials: (t/(eᵗ − 1))^x = ∑ B(n)(x)·tⁿ/n!. With f = (eᵗ − 1)/t and
  g = f^(−x) = ∑ g(n)tⁿ, differentiating gives f·g′ = −x·f′·g; comparing coefficients of tᵐ⁻¹ with
  f's coefficients 1/(k + 1)! gives m·g(m) = −∑_(i<m) g(i)(i + (m − i)x)/(m − i + 1)!, and with
  B(m) = m!·g(m):

  B(m) = −∑_(i<m) C(m + 1, i)·(i + (m − i)x)·B(i) / (m(m + 1)), B(0) = 1.

  It gives the entry's B(1) = −x/2 and B(2) = (3x² − x)/12, and the first 46 denominators were
  checked against the entry's own recurrence (with Bernoulli numbers).
- The denominator of a polynomial is the least common multiple of the denominators of its
  coefficients (the Mathematica line in the entry takes the denominator of the content after
  `Factor`, which is the same number).
- Each row of `B` is [i, coefficients of B(i) from x⁰ up]; `for i,*P in B` unpacks the index
  and the coefficients. The coefficient of xʲ in the new row is
  ∑ C(m + 1, i)·(i·P[j] + (m − i)·P[j − 1]) / (−m(m + 1)); `sum(P[j:j+1])` and `sum(P[j-1:j])`
  read a coefficient as 0 when it lies outside the row. `Fraction(m*~m)` is −m(m + 1) and makes
  every coefficient an exact fraction. The index i at the front of each row is an int, whose
  denominator 1 does not change the lcm that is printed.

**Notes**

- Exact rational arithmetic, so the program is right for every n. The b-file has only the 27
  terms of the entry (to n = 26); they come in a fraction of a second.
- The 27 terms fit in a table shorter than the program, so it needs a review.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 222 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001898), CC BY-SA 4.0.
