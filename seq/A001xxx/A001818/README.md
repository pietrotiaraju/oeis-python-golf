# A001818

> Squares of double factorials: (1*3*5*...*(2n-1))^2 = ((2*n-1)!!)^2.
> — [OEIS A001818](https://oeis.org/A001818)

Offset 0: 1, 1, 9, 225, 11025, 893025, 108056025, 18261468225, 4108830350625, 1187451971330625, 428670161650355625, 189043541287806830625, …

### Python 3 — 33 bytes

```python
a=n=1
while[print(a)]:a*=n*n;n+=2
```

**How it works**

- **The formula.** a(n) = ((2n − 1)!!)², so a(n) = a(n − 1)·(2n − 1)², from
  a(0) = 1 (the empty product).
- **The program.** `n` runs over the odd numbers 1, 3, 5, …; after printing
  a(k) it multiplies by n² = (2k + 1)², which gives a(k + 1).

**Notes**

- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+ near n = 780.
- Keeping (2n − 1)!! and printing its square, `print(b*b)` with `b*=n`, has
  the same length.
- The b-file has 51 terms (n = 0 to 50); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001818), CC BY-SA 4.0.
