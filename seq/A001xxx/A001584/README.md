# A001584

> A generalized Fibonacci sequence.
> — [OEIS A001584](https://oeis.org/A001584)

Offset 0: 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 4, 4, 4, 7, 7, 8, 12, 12, 16, 21, …

### Python 3 — 47 bytes

```python
l=[1]*8
for x in l:l+=2*l[-3]-l[-6]+x,;print(x)
```

**How it works**

- The entry defines the sequence by its generating function
  (1 + x + x² − x³ − x⁴ − x⁵)/(1 − 2x³ + x⁶ − x⁸). Multiplying out the
  denominator gives a(n) = 2a(n−3) − a(n−6) + a(n−8) for n ≥ 8, and
  dividing out the first eight coefficients gives a(0) = … = a(7) = 1.
- `l` starts with those eight 1s and the loop runs over the list while it
  grows. When `x` = l[i] = a(i) is read, the list holds a(0), …, a(i+7),
  so `l[-3]` = a(i+5) and `l[-6]` = a(i+2), and the appended value is
  2a(i+5) − a(i+2) + a(i) = a(i+8). Then a(i) is printed, so the terms
  come out in order from a(0), and the list stays 8 terms ahead.

**Notes**

- The denominator factors as (1 − x³ − x⁴)(1 − x³ + x⁴) and the numerator
  as (1 + x + x²)(1 − x³), so the g.f. is
  (1 + x + x²)·½(1/(1 − x³ − x⁴) + 1/(1 − x³ + x⁴)): a(n) counts the
  compositions of n, n − 1 and n − 2 into parts 3 and 4 that use an even
  number of 4s. The program does not need this.
- The sliding window `while 1:a,*l=*l,2*l[5]-l[2]+l[0];print(a)` of
  [A000073](../../A000xxx/A000073/) is 49 bytes. The growing list keeps
  every term in memory, which is harmless at this growth rate.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (a(0) to a(1000)); the bar is the whole b-file
  in 60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001584), CC BY-SA 4.0.
