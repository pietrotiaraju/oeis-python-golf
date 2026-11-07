# A000909

> a(n) = (2*n)!*(2*n+1)! / n!^2.
> — [OEIS A000909](https://oeis.org/A000909)

Offset 0: 1, 12, 720, 100800, 25401600, 10059033600, 5753767219200, …

### Python 3 — 37 bytes

```python
a=1;m=0
while[print(a)]:m+=4;a*=m*m-4
```

**How it works**

- The ratio of consecutive terms is a whole number:
  a(n)/a(n−1) = (2n)(2n−1)·(2n+1)(2n)/n² = 4(2n−1)(2n+1) = 16n² − 4.
- With m = 4n that factor is m² − 4, so `m` steps by 4 and `a*=m*m-4`
  needs no division at all.

**Notes**

- Exact integer arithmetic, correct for every n.
- The b-file has 101 terms (up to a(100)); the bar is the whole b-file in
  60 s. The program prints 712 terms at once and then stops with a
  `ValueError` at the 4300-digit int-to-str limit of Python 3.11+.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000909), CC BY-SA 4.0.
