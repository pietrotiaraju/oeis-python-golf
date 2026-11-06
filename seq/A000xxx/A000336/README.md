# A000336

> a(n) = a(n-1)*a(n-2)*a(n-3)*a(n-4); for n < 5, a(n) = n.
> — [OEIS A000336](https://oeis.org/A000336)

Offset 1: 1, 2, 3, 4, 24, 576, 165888, 9172942848, 21035720123168587776, …

### Python 3 — 53 bytes

```python
a,b,c,d=1,2,3,4
while[print(a)]:a,b,c,d=b,c,d,a*b*c*d
```

**How it works**

- `a,b,c,d` is a window of four consecutive terms, a(n) to a(n+3), starting
  from a(1) … a(4) = 1, 2, 3, 4.
- `print(a)` runs in the loop condition and prints a(n); `[None]` is a
  non-empty list, so the loop never stops.
- The body moves the window one step: the three newest terms slide down and
  their product with the oldest one, a(n)·a(n+1)·a(n+2)·a(n+3) = a(n+4), comes
  in at the end.

**Notes**

- The [A000078](../A000078/) frame with a product instead of a sum,
  `import math` + `l=1,2,3,4` + `while 1:a,*l=*l,math.prod(l);print(a)`, is
  59 bytes (61 with `from math import*`), so the four named variables win
  here although they lose for the tetranacci sum.
- Starting one step early does not help: the term before a(1) would have to
  be 2/3 for the window to reach 1, 2, 3, 4.
- Exact integers, so every term is right. The number of digits grows by a
  factor of about 1.93 (the tetranacci constant) per term: a(17) has 3682
  digits and a(18) has 7097, so Python's 4300-digit
  int-to-str limit stops the program after a(17) with a `ValueError`, which
  is not counted as a failure.
- The b-file has 15 terms (n = 1 to 15, the last one has 991 digits) and they
  print at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000336), CC BY-SA 4.0.
