# A000505

> Eulerian numbers (Euler's triangle: column k=5 of A008292, column k=4 of A173018).
> — [OEIS A000505](https://oeis.org/A000505)

Offset 5: 1, 57, 1191, 15619, 156190, 1310354, 9738114, 66318474, 423281535, 2571742175, …

### Python 3 — 93 bytes

```python
from math import*
n=5
while 1:print(sum((-1)**j*comb(n+1,j)*(5-j)**n for j in range(5)));n+=1
```

**How it works**

- The Eulerian number counting permutations of n elements with 4
  descents is Σⱼ₌₀^4 (−1)^j C(n+1,j)(5−j)^n, by the usual
  inclusion–exclusion formula for Eulerian numbers.
- The OEIS offset is 5. Starting there skips the initial zero values;
  the first printed value is the unique decreasing permutation.
- `comb` computes binomial coefficients exactly. The alternating sum is
  evaluated anew for each n, with only 5 summands.

**Notes**

- No factorial-sized permutation search or floating point arithmetic is
  needed. Large integers eventually meet Python's conversion limit.
- The reference file contains 996 terms from the OEIS b-file; the verification
  bar is 996 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000505), CC BY-SA 4.0.
