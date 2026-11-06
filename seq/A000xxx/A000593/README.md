# A000593

> Sum of odd divisors of n.
> — [OEIS A000593](https://oeis.org/A000593)

Offset 1: 1, 1, 4, 1, 6, 4, 8, 1, 13, 6, …

### Python 3 — 62 bytes

```python
n=0
while 1:n+=1;print(sum(d for d in range(1,n+1,2)if n%d<1))
```

**How it works**

- A divisor contributes precisely when it is positive, odd, and divides
  n. The step-2 range generates only odd candidates and the remainder
  test selects the divisors.
- Summing those candidates is the defining odd-divisor sum. The loop
  increments n before printing, so it begins at the OEIS offset 1.
- Powers of two correctly print 1, since their only odd divisor is 1.

**Notes**

- This is exact trial division with no factorization dependency.
- The linear scan is intentionally compact; the complete 10000-term
  reference table remains practical for verification.
- The reference file contains 10000 terms from the OEIS b-file; the verification
  bar is 10000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000593), CC BY-SA 4.0.
