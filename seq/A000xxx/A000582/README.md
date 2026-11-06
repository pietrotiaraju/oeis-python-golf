# A000582

> a(n) = binomial coefficient C(n,9).
> — [OEIS A000582](https://oeis.org/A000582)

Offset 9: 1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620, …

### Python 3 — 41 bytes

```python
n=9;a=1
while[print(a)]:n+=1;a=a*n//(n-9)
```

**How it works**

- Start with C(9,9)=1 at the OEIS offset n=9.
  Consecutive entries of the binomial column obey

  **C(n,9)=n·C(n−1,9)/(n−9)**, for n>9.

- Print the stored coefficient, increment n, then multiply and
  divide by that ratio. The first division has denominator 1;
  every later division is exact by the binomial identity.
- The program needs only the counter and one coefficient. No
  imports or separate handling of the column's earlier zeros are
  needed, since output starts at n=9.

**Notes**

- Every term is computed with exact integer arithmetic.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 992 terms from the OEIS b-file; the verification
  bar is 992 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000582), CC BY-SA 4.0.
