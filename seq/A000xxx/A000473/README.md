# A000473

> Number of genus 0 rooted maps with 5 faces and n vertices.
> — [OEIS A000473](https://oeis.org/A000473)

Offset 4: 14, 386, 5868, 65954, 614404, 5030004, 37460376, 259477218, 1697186964, 10596579708, …

### Python 3 — 98 bytes

```python
from math import*
n=4
while[print(comb(n,3)*(comb(t:=2*n,n)*(t*t+7*t+3)-(60*t+45<<t-4))//60)]:n+=1
```

**How it works**

- The program evaluates the closed form
  a(n) = C(n,3)·((4n² + 14n + 3)·C(2n,n) − 15(8n + 3)·4ⁿ⁻²)/60.
- Where it comes from: Sean Irvine's generating function on the OEIS page
  is x³(1−s)(17 + 16x − (10+4x)s)/s¹¹ with s = √(1−4x). Using s² = 1 − 4x
  the numerator is 27 − 20x − 16x² − (27 + 20x)s, so the series is
  x³(27 − 20x − 16x²)(1−4x)^(−11/2) − x³(27 + 20x)(1−4x)^(−5). The
  coefficients of xᵐ in the two powers are C(2m+10, m+5)·C(m+5, 5)/252
  and 4ᵐ·C(m+4, 4). Dividing the central-binomial part by C(2n,n) and the
  power part by 4ⁿ leaves rational functions of n, and both agree with
  the closed form (checked symbolically).
- 15(8n+3)·4ⁿ⁻² as the shift `120*n+45<<2*n-4` is 2 bytes under
  `15*(8*n+3)*4**(n-2)` (the shift count is ≥ 4 since n ≥ 4). With
  t = 2n, set by the walrus inside the first `comb`, the polynomial
  becomes `t*t+7*t+3` and the shift `60*t+45<<t-4`, 3 bytes shorter each,
  for 3 bytes of walrus.
- By the identity the product before `//60` is 60·a(n), so the division
  is exact.

**Notes**

- `import math` would cost 4 bytes more here, since `comb` is used twice.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 497 terms (up to a(500)); the bar is the whole b-file in
  60 s. It prints in a fraction of a second.
- a(n) first has more than 4300 digits at n = 7118, so printing stops
  there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 104 | first entry |
| 2026-11-07 | Python 3 | 98 | t = 2n by walrus, power of 4 as a shift |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000473), CC BY-SA 4.0.
