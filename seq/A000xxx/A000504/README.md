# A000504

> S2(j,2j+3) where S2(n,k) is a 2-associated Stirling number of the second kind.
> — [OEIS A000504](https://oeis.org/A000504)

Offset 1: 1, 56, 1918, 56980, 1636635, 47507460, 1422280860, 44346982680, 1446733012725, 49473074851200, …

### Python 3 — 84 bytes

```python
n=a=1
while[print(a)]:n+=1;a=a*(2*n+3)*(n+1)*(10*n*n+15*n+2)//((n-1)*(10*n*n-5*n-3))
```

**How it works**

- These are partitions of 2n+3 labeled elements into n blocks, every
  block of size at least 2. There are three excess elements beyond n
  pairs: either one block of size 5, a block of size 4 and one of size 3,
  or three blocks of size 3.
- Adding the three multinomial counts gives
  a(n)=(2n+3)!*n*(10n²+15n+2)/(1620*2^n*n!). Their consecutive ratio is
  (2n+3)(n+1)(10n²+15n+2)/((n-1)(10n²-5n-3)).
- Starting with a(1)=1, the body advances n before applying that ratio.
  This proves the first-order recurrence listed in OEIS directly from
  the block interpretation.

**Notes**

- The numerator is divisible by the denominator at every step. The
  recurrence uses only integer arithmetic and stores one sequence value.
- Python's integer conversion limit can eventually stop printing.
- The reference file contains 17 terms from the OEIS b-file; the verification
  bar is 17 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 84 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000504), CC BY-SA 4.0.
