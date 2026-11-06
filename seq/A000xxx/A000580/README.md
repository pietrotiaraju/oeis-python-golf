# A000580

> a(n) = binomial coefficient C(n,7).
> — [OEIS A000580](https://oeis.org/A000580)

Offset 7: 1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440, …

### Python 3 — 41 bytes

```python
n=7;a=1
while[print(a)]:n+=1;a=a*n//(n-7)
```

**How it works**

- Start with C(7,7)=1 at the OEIS offset n=7.
  Consecutive entries of the binomial column obey

  **C(n,7)=n·C(n−1,7)/(n−7)**, for n>7.

- Print the stored coefficient, increment n, then multiply and
  divide by that ratio. The first division has denominator 1;
  every later division is exact by the binomial identity.
- The program needs only the counter and one coefficient. No
  imports or separate handling of the column's earlier zeros are
  needed, since output starts at n=7.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 994 terms from the OEIS b-file; the verification
  bar is 994 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000580), CC BY-SA 4.0.
