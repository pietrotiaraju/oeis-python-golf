# A000551

> Number of labeled rooted trees of height 2 with n nodes.
> — [OEIS A000551](https://oeis.org/A000551)

Offset 3: 6, 36, 200, 1170, 7392, 50568, 372528, 2936070, 24617120, 218521116, …

### Python 3 — 99 bytes

```python
from math import*
n=3
while[print(n*(n-1)*sum(comb(n-2,k-1)*k**(n-2-k)for k in range(1,n-1)))]:n+=1
```

**How it works**

- Choose the root in n ways and its k children from the remaining n−1
  labels. Every other vertex must be a leaf attached to one of those
  children, giving n·C(n−1,k)·k^(n−1−k) trees.
- Height exactly 2 requires at least one such leaf, so 1≤k≤n−2.
  The identity C(n−1,k)=(n−1)C(n−2,k−1)/k rewrites the sum as
  n(n−1)·Σₖ₌₁ⁿ⁻² C(n−2,k−1)·k^(n−2−k), the formula listed by OEIS.
- All exponents are nonnegative. Starting at n=3 gives the six possible
  rooted paths on three labels; printing in a nonempty list keeps the
  loop running after each term.

**Notes**

- Binomial coefficients and powers are evaluated with exact integers;
  each term is computed independently without storing earlier trees.
- Large outputs eventually meet Python's integer conversion limit.
- The reference file contains 198 terms from the OEIS b-file; the verification
  bar is 198 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 99 | first entry; direct count by root degree |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000551), CC BY-SA 4.0.
