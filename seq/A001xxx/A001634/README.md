# A001634

> a(n) = a(n-2) + a(n-3) + a(n-4), with initial values a(0) = 0, a(1) = 2, a(2) = 3, a(3) = 6.
> — [OEIS A001634](https://oeis.org/A001634)

Offset 0: 0, 2, 3, 6, 5, 11, 14, 22, 30, 47, 66, 99, 143, 212, 308, 454, 663, …

### Python 3 — 45 bytes

```python
l=0,2,3,6
while 1:a,*l=*l,sum(l[:3]);print(a)
```

**How it works**

- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(0) to a(3) = 0, 2, 3, 6.
- `*l,sum(l[:3])` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l[:3])` = a(n) + a(n+1) + a(n+2), which is a(n+4) by the recurrence a(n+4) = a(n+2) + a(n+1) + a(n).
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(0).
- Integers are exact, so every term is right, for every n.

**Notes**

- The characteristic polynomial factors as x⁴ − x² − x − 1 =
  (x + 1)(x³ − x² − 1), and the g.f. x(2 + 3x + 4x²)/(1 − x² − x³ − x⁴)
  says that a(n) is the sum of the (n+1)-th powers of its four roots, so
  a(n) = (−1)ⁿ⁺¹ + [A001609](../A001609/)(n+1). Printing that needs a sign
  variable on top of A001609's three, which is longer.
- `sum(l)-l[3]` is one byte longer than the prefix sum `sum(l[:3])`. The
  growing list `l=[0,2,3,6]` / `for x in l:l+=x+l[-2]+l[-3],;print(x)` is
  49 bytes. A search over chains of four in-place statements on four
  variables (`x+=y`, `x-=y`, `x=y-x`, `x±=2*y`, `x=-x`, any start) found
  none with this characteristic polynomial below 45 bytes.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(25901), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 501 terms (a(0) to a(500)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 45 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001634), CC BY-SA 4.0.
