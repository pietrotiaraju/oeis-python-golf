# A000581

> a(n) = binomial coefficient C(n,8).
> — [OEIS A000581](https://oeis.org/A000581)

Offset 8: 1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310, …

### Python 3 — 41 bytes

```python
n=8;a=1
while[print(a)]:n+=1;a=a*n//(n-8)
```

**How it works**

- Start with C(8,8)=1 at the OEIS offset n=8.
  Consecutive entries of the binomial column obey

  **C(n,8)=n·C(n−1,8)/(n−8)**, for n>8.

- Print the stored coefficient, increment n, then multiply and
  divide by that ratio. The first division has denominator 1;
  every later division is exact by the binomial identity.
- The program needs only the counter and one coefficient. No
  imports or separate handling of the column's earlier zeros are
  needed, since output starts at n=8.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 993 terms from the OEIS b-file; the verification
  bar is 993 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000581), CC BY-SA 4.0.
