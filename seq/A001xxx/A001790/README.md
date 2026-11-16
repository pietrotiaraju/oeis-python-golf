# A001790

> Numerators in expansion of 1/sqrt(1-x).
> — [OEIS A001790](https://oeis.org/A001790)

Offset 0: 1, 1, 3, 5, 35, 63, 231, 429, 6435, 12155, …

### Python 3 — 46 bytes

```python
a=1;j=0
while[print(a)]:j+=2;a=a*~-j*(j&-j)//j
```

**How it works**

- C(2n, n)/4ⁿ has a power of 2 as denominator, and C(2n, n) has only
  popcount(n) < 2n factors 2, so in lowest terms the numerator is the odd
  part of C(2n, n).
- n·C(2n, n) = 2(2n−1)·C(2n−2, n−1), and odd parts multiply, so
  a(n) = a(n−1)·(2n−1)/odd(n). With j = 2n, odd(n) = odd(j) = j/(j&−j), so
  the step is `a=a*~-j*(j&-j)//j`. The quotient is the integer a(n), so the
  floor division is exact.

**Notes**

- Exact integer arithmetic, correct for every n. a(7152) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Ties at 46 bytes with odd j = 2n − 1 updated before the step,
  `a=j=1` / `while[print(a)]:a=a*j*(-~j&~j)//-~j;j+=2` (`-~j&~j` is the
  lowest set bit of j + 1). Keeping C(2n, n) and printing its odd part,
  `c//(c&-c)`, is 51 bytes.
- The b-file has 1667 terms (a(0) to a(1666)); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001790), CC BY-SA 4.0.
