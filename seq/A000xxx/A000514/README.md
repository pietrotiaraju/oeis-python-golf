# A000514

> Eulerian numbers (Euler's triangle: column k=6 of A008292, column k=5 of A173018).
> — [OEIS A000514](https://oeis.org/A000514)

Offset 6: 1, 120, 4293, 88234, 1310354, 15724248, 162512286, 1505621508, 12843262863, 102776998928, …

### Python 3 — 93 bytes

```python
from math import*
n=6
while 1:print(sum((-1)**j*comb(n+1,j)*(6-j)**n for j in range(6)));n+=1
```

**How it works**

- The Eulerian number counting permutations of n elements with 5
  descents is Σⱼ₌₀^5 (−1)^j C(n+1,j)(6−j)^n, by the usual
  inclusion–exclusion formula for Eulerian numbers.
- The OEIS offset is 6. Starting there skips the initial zero values;
  the first printed value is the unique decreasing permutation.
- `comb` computes binomial coefficients exactly. The alternating sum is
  evaluated anew for each n, with only 6 summands.

**Notes**

- No factorial-sized permutation search or floating point arithmetic is
  needed. Large integers eventually meet Python's conversion limit.
- The reference file contains 995 terms from the OEIS b-file; the verification
  bar is 995 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000514), CC BY-SA 4.0.
