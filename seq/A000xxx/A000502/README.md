# A000502

> Number of genus 0 rooted maps with 6 faces and n vertices.
> — [OEIS A000502](https://oeis.org/A000502)

Offset 5: 42, 1586, 31388, 442610, 5030004, 49145460, 429166584, 3435601554, 25658464260, 181055975100, …

### Python 3 — 109 bytes

```python
from math import*
n=5
while 1:print(comb(n,4)*(2*(64*n*n+432*n+83)*4**(n-4)-(2*n+1)**2*comb(2*n,n))//30);n+=1
```

**How it works**

- Write s=√(1−4x). The OEIS generating function is
  x⁴((189−168x−304x²)/(1−4x)⁷ − (189+168x)/(1−4x)^(13/2)).
- Apply the generalized binomial theorem to the two terms and simplify
  their factorial ratios. The coefficient of x^n is
  C(n,4)(2(64n²+432n+83)4^(n−4)−(2n+1)²C(2n,n))/30.
- n=5 is the stated offset. This coefficient formula avoids both
  enumerating planar maps and doing formal square-root arithmetic.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 496 terms from the OEIS b-file; the verification
  bar is 496 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 109 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000502), CC BY-SA 4.0.
