# A000520

> Nearest integer to log_10(n).
> — [OEIS A000520](https://oeis.org/A000520)

Offset 1: 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, …

### Python 3 — 39 bytes

```python
n=1
while[print(len(str(n*n))//2)]:n+=1
```

**How it works**

- If d is the number of decimal digits of n², then
  d−1 ≤ 2 log₁₀(n) < d. It follows that
  floor(log₁₀(n)+1/2)=floor(d/2).
- No tie is possible: a positive integer cannot equal 10^(k+1/2).
  Squaring and counting digits therefore gives exact nearest-integer
  rounding without floating point logarithms.
- The loop starts at n=1 and advances after printing in the nonempty
  list condition.

**Notes**

- This uses exact integer multiplication and decimal conversion.
- Python's default conversion limit is eventually reached for n² with
  more than 4300 digits; that interpreter limit is excluded by the rules.
- The reference file contains 1000 terms from the OEIS b-file; the verification
  bar is 1000 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000520), CC BY-SA 4.0.
