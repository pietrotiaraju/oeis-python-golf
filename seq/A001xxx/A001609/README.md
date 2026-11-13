# A001609

> a(1) = a(2) = 1, a(3) = 4; thereafter a(n) = a(n-1) + a(n-3).
> — [OEIS A001609](https://oeis.org/A001609)

Offset 1: 1, 1, 4, 5, 6, 10, 15, 21, 31, 46, 67, 98, 144, 211, 309, 453, 664, …

### Python 3 — 39 bytes

```python
a=3;b=c=1
while[print(b)]:a,b,c=b,c,a+c
```

**How it works**

- (a, b, c) holds (a(n−1), a(n), a(n+1)) and `b` is printed; the tuple
  shift `a,b,c=b,c,a+c` appends a(n+2) = a(n+1) + a(n−1).
- The window starts one step early, at n = 1, with the value a(0) that the
  recurrence gives backwards: a(3) = a(2) + a(0), so a(0) = 4 − 1 = 3.
  That is also the natural a(0): a(n) is the sum of the n-th powers of the
  three roots of x³ = x² + 1 (the trace of the n-th power of the companion
  matrix, as in the entry), and there are three roots.

**Notes**

- The window that starts at the data's a(1), a(2), a(3),
  `a=b=1;c=4` with `a` printed, ties at 39 bytes. A search over
  three-variable tuples with short entries found nothing below 39, and
  chains of three in-place statements with coefficients ±1 need 44.
- The entry carries the keyword "changed"; its name and its data
  (1, 1, 4, 5, 6, 10, …) agree, and the program follows both.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 6012 terms (a(1) to a(6012)); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001609), CC BY-SA 4.0.
