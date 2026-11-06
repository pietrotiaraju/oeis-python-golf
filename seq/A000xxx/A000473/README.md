# A000473

> Number of genus 0 rooted maps with 5 faces and n vertices.
> — [OEIS A000473](https://oeis.org/A000473)

Offset 4: 14, 386, 5868, 65954, 614404, 5030004, 37460376, 259477218, 1697186964, 10596579708, …

### Python 3 — 104 bytes

```python
from math import*
n=4
while 1:print(comb(n,3)*((4*n*n+14*n+3)*comb(2*n,n)-15*(8*n+3)*4**(n-2))//60);n+=1
```

**How it works**

- Put s=√(1−4x). The generating function on the OEIS page is
  x³(1−s)(17+16x−(10+4x)s)/(1−4x)^(11/2).
  Use s²=1−4x to expand its numerator into
  27−20x−16x²−(27+20x)s.
- The series therefore becomes

  x³·((27−20x−16x²)(1−4x)^(−11/2)
  −(27+20x)(1−4x)^(−5)).

- For the integer power, the coefficient of xᵐ in (1−4x)⁻⁵
  is 4ᵐ·C(m+4,4), by the binomial theorem. The half-integer power
  follows by differentiating (1−4x)^(−1/2) five times:
  its m-th coefficient is
  ((m+5)!/m!)·C(2m+10,m+5)/30240.
- Take the shifted coefficients at m=n−3, n−4 and n−5,
  with negative indices interpreted as zero. Combining and
  simplifying them gives

  **a(n)=C(n,3)·((4n²+14n+3)C(2n,n)
  −15(8n+3)4^(n−2))/60.**

- The code evaluates that integer expression directly. Its index
  starts at n=4, where the generating function has its first
  nonzero coefficient: C(4,3)·(123·70−15·35·16)/60
  =4·210/60=14.

**Notes**

- Exact binomial coefficients, powers and a final exact division.
  The square root and fractional power are used to derive the
  coefficient formula; the program evaluates neither numerically.
- Cancellation between the central-binomial and power-of-four
  contributions occurs before dividing by 60. Dividing those pieces
  separately would needlessly introduce fractional intermediates.
- The loop retains only an index and integer temporaries. It avoids
  building maps or expanding a power series anew for each term.
  The exponentially growing output eventually reaches Python 3.11+'s
  default 4300-digit conversion limit, an interpreter limit.
- The b-file has 497 terms (indices 4 through 500). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 104 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000473), CC BY-SA 4.0.
