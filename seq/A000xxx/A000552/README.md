# A000552

> Number of labeled rooted trees of height 3 with n nodes.
> — [OEIS A000552](https://oeis.org/A000552)

Offset 4: 24, 300, 3360, 38850, 475776, 6231960, 87530400, 1316954430, 21173760960, 362670636900, …

### Python 3 — 179 bytes

```python
from math import*
A=[[1]*3];n=0
while 1:
 n+=1;B=[1]+[sum(comb(n-1,k-1)*k*A[k-1][j-1]*A[n-k][j]for k in range(1,n+1))for j in range(1,3)];A+=B,
 if n>=3:print((n+1)*(B[-1]-B[-2]))
```

**How it works**

- Let T_j(x) count labeled rooted trees of height at most j:
  T₀=x and T_j=x·exp(T_(j−1)). Write E_j=exp(T_j).
- `A[m][j]` stores the m-th exponential coefficient of E_j. E₀=exp(x),
  so column 0 is always 1, and every series has constant coefficient 1.
- Differentiating E_j and comparing coefficients gives
  E_j(n)=Σₖ₌₁ⁿ C(n−1,k−1)·k·E_(j−1)(k−1)·E_j(n−k).
  The list comprehension uses only earlier size rows, so all dependencies
  are already known and every operation is integral.
- Rooting on n+1 labels multiplies E_(2)(n) by n+1. Subtracting
  E_(1)(n) selects height exactly 3, instead of height at most 3.
  The first printed size is 4, the OEIS offset.

**Notes**

- The nested exponential series are handled by finite exact binomial
  convolutions; no real-valued exponential is evaluated.
- Large outputs eventually meet Python's integer conversion limit.
- The reference file contains 16 terms from the published OEIS entry; the verification
  bar is 16 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 179 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000552), CC BY-SA 4.0.
