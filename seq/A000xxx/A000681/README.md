# A000681

> Number of n X n matrices with nonnegative entries and every row and column sum 2.
> — [OEIS A000681](https://oeis.org/A000681)

Offset 0: 1, 1, 3, 21, 282, 6210, 202410, 9135630, 545007960, …

### Python 3 — 50 bytes

```python
a=b=n=1
while[print(a)]:a*=n*n;a,b=a-n*b//2,a;n+=1
```

**How it works**

- The counts have the exponential generating function
  Σ a(n)xⁿ/n!² = e^{x/2}/√(1−x) (OEIS entry). It satisfies
  2(1−x)y′ = (2−x)y, which on coefficients is the OEIS recurrence
  a(n) = n²a(n−1) − n(n−1)²a(n−2)/2.
- `a*=n*n` turns a(n−1) into c = n²a(n−1), the first part of a(n). The old
  value of `b` is the c of the previous step, (n−1)²a(n−2), so the second
  part is `n*b//2`; then `b` keeps the new c for the next step.
- `b` starts at 1 rather than 0: at n = 1 the term `1*1//2` is 0 anyway,
  which lets `a=b=n=1` set up all three names.

**Notes**

- The halving is exact: n²a(n−1) − a(n) = n(n−1)²a(n−2)/2 is an integer,
  so `n*b//2` never rounds.
- Python's 4300-digit limit on int-to-str conversion stops the program after
  860 terms, in under a second.
- The b-file has 251 terms; the bar is all 251 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000681), CC BY-SA 4.0.
