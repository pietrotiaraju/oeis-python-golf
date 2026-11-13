# A001641

> A Fielder sequence: a(n) = a(n-1) + a(n-2) + a(n-4).
> — [OEIS A001641](https://oeis.org/A001641)

Offset 1: 1, 3, 4, 11, 16, 30, 50, 91, 157, 278, 485, 854, 1496, 2628, 4609, …

### Python 3 — 47 bytes

```python
l=1,3,4,11
while 1:a,*l=*l,sum(l)-l[1];print(a)
```

**How it works**

- The g.f. x(1 + 2x + 4x³)/(1 − x − x² − x⁴) fixes where the recurrence
  starts: it holds for n ≥ 5, from a(1), …, a(4) = 1, 3, 4, 11.
- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(1) to a(4) = 1, 3, 4, 11.
- `*l,sum(l)-l[1]` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l)-l[1]` = a(n) + a(n+2) + a(n+3), which is a(n+4) by the recurrence a(n+4) = a(n+3) + a(n+2) + a(n).
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The numerator is −xD′(x), so a(n) is the sum of the n-th powers of the
  roots of x⁴ = x³ + x² + 1. As x⁴ − x³ − x² − 1 = (x + 1)(x³ − 2x² + x − 1),
  a(n) = (−1)ⁿ + the n-th power sum of the roots of x³ = 2x² − x + 1. The
  program does not need this.
- A search over chains of four in-place statements on four variables
  (`x+=y`, `x-=y`, `x=y-x`, `x±=2*y`, `x=-x`, any start) found none with
  this characteristic polynomial below 47 bytes. The growing list
  `l=[1,3,4,11]` / `for x in l:l+=x+l[-2]+l[-1],;print(x)` is 50.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(17605), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 47 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001641), CC BY-SA 4.0.
