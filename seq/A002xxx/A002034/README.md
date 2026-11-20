# A002034

> Kempner numbers: smallest positive integer m such that n divides m!.
> — [OEIS A002034](https://oeis.org/A002034)

Offset 1: 1, 2, 3, 4, 5, 3, 7, 4, 6, 5, 11, 4, 13, 7, 5, 6, 17, 6, 19, 5, 7, 11, …

### Python 3 — 58 bytes

```python
n=0
while n:=n+1:
 m=f=1
 while f%n:m+=1;f=f*m%n
 print(m)
```

**How it works**

- For each n the inner loop walks m = 1, 2, 3, … keeping f = m! mod n
  (`f=f*m%n` multiplies in the next factor and reduces at once), and
  stops at the first m with n | m!. That m is a(n).
- f starts at 1, not 1 mod n, so the test is `f%n`: for n = 1 it is
  0 at once and a(1) = 1.
- The search always ends: n | n!, so m ≤ n.

**Notes**

- Keeping f reduced mod n keeps it below n, so each step is cheap; the
  unreduced m! would have tens of thousands of digits for n near 10⁴.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s,
  about 3 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002034), CC BY-SA 4.0.
