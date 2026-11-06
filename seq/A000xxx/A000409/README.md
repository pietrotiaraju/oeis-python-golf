# A000409

> Singular n X n (0,1)-matrices: the number of n X n (0,1)-matrices having distinct, nonzero ordered rows, but having at least two equal columns or at least one zero column.
> — [OEIS A000409](https://oeis.org/A000409)

Offset 2: 0, 6, 350, 43260, 14591171, 14657461469, 46173502811223, 474928141312623525, 16489412944755088235117, 1985178211854071817861662307, …

### Python 3 — 144 bytes

```python
import math
s=0,2,-3,1;n=2
while[print(-sum(s[k+1]*math.comb(2**k-1,n)for k in range(n)))]:
 n+=1;s=[0]+[s[k-1]-n*s[k]for k in range(1,n+1)]+[1]
```

**How it works**

- The formula on the OEIS page is
  a(n)=−Σₖ₌₀ⁿ⁻¹ s(n+1,k+1)·C(2ᵏ−1,n), with signed
  first-kind Stirling numbers. These are the coefficients of
  x(x−1)…(x−n), stored in increasing powers in `s`.
- At n=2 that polynomial is x³−3x²+2x, so
  `s=0,2,-3,1`. The comprehension takes `s[k+1]`, multiplies it
  by the indicated binomial coefficient and negates the complete sum.
- A binary vector of length k has 2ᵏ−1 nonzero possibilities; the
  binomial term chooses n distinct such vectors. The Stirling coefficients
  perform the inversion that singles out the column degeneracies in
  the definition.
- After printing, increment n. Multiplication of the old polynomial
  by x−n replaces coefficient s[k] by s[k−1]−n·s[k]. The leading
  zero and final 1 in the new list handle the two endpoint powers.
- `math.comb(2**k-1,n)` is zero if there are fewer than n available
  patterns. All its arguments are nonnegative, even for k=0, so
  the low-index zero contributions need no special case.

**Notes**

- This sequence counts matrices with a zero column or repeated columns
  subject to the specified row condition. Linear dependence without
  either of those column defects does not suffice for this count.
- For n=3, the nonzero contribution is −s(4,3)·C(3,3)=6.
  It is an inclusion-exclusion count, so intermediate signed terms
  are expected even though the result is nonnegative.
- Exact integers; the polynomial multiplication constructs the needed
  Stirling row at every size. One growing coefficient list is retained.
- The initial tuple is shorter than a list literal; the first update
  creates a list. `import math` also saves bytes here because only
  `comb` is used, once in the source.
- The b-file has 14 terms (indices 2 through 15). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 147 | first entry |
| 2026-11-06 | Python 3 | 144 | import math and start the coefficients as a tuple |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000409), CC BY-SA 4.0.
