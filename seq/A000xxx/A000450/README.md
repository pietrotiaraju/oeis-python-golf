# A000450

> a(n) = A058057(n,n-4).
> — [OEIS A000450](https://oeis.org/A000450)

Offset 4: 1, 10, 50, 385, 3130, 28764, 291900, 3249210, 39367395, 515874470, …

### Python 3 — 114 bytes

```python
from math import*
n=4
while 1:print(sum((-1)**k*factorial(n-k)*comb(k,4)*comb(2*n-k,k)for k in range(4,n+1)));n+=1
```

**How it works**

- The straight-table ménage hit polynomial is
  U_n(t)=Σₖ₌₀ⁿ C(2n−k,k)(n−k)!(t−1)ᵏ.
  The triangle A058057 is read from the highest power down, so
  its entry (n,n−4) is the coefficient of t⁴.
- In (t−1)ᵏ that coefficient is (−1)^(k−4)C(k,4).
  Because 4 is even, its sign is simply (−1)ᵏ. Terms with k<4
  contribute zero, leaving exactly the sum in the program.
- The loop starts at n=4. For every `k in range(4,n+1)`, n−k
  is nonnegative and 2n−k≥k, so the factorial and both binomial
  coefficients are defined throughout the sum.
- At n=4 only k=4 contributes, giving 1. At n=5 the two
  contributions are C(6,4)−C(5,4)=15−5=10.

**Notes**

- Exact inclusion-exclusion with integer factorials and binomial
  coefficients. Large positive and negative summands cancel before
  the output is printed; there is no floating-point approximation.
- Each term evaluates n−3 summands afresh, so the program stores
  no previous terms or polynomial coefficients. A recurrence could
  reuse work, but the finite sum keeps the implementation short.
- [A000426](../A000426/) is another ménage hit coefficient,
  for the circular polynomial and a different power of t.
- Factorial growth eventually reaches Python 3.11+'s default
  4300-digit integer-to-string limit, an interpreter limit.
- The b-file has 447 terms (indices 4 through 450). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000450), CC BY-SA 4.0.
