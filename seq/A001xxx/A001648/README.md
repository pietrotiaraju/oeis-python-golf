# A001648

> Tetranacci numbers A073817 without the leading term 4.
> — [OEIS A001648](https://oeis.org/A001648)

Offset 1: 1, 3, 7, 15, 26, 51, 99, 191, 367, 708, 1365, 2631, 5071, 9775, …

### Python 3 — 42 bytes

```python
l=1,3,7,15
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- The name refers to [A073817](https://oeis.org/A073817), 4, 1, 3, 7, 15,
  …, the tetranacci numbers a(n) = a(n−1) + a(n−2) + a(n−3) + a(n−4) that
  start with the power sums 4, 1, 3, 7; this sequence drops the 4 and
  starts at a(1) = 1, as the g.f. x(1 + 2x + 3x² + 4x³)/(1 − x − x² − x³ − x⁴)
  says.
- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(1) to a(4) = 1, 3, 7, 15.
- `*l,sum(l)` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l)` = a(n) + a(n+1) + a(n+2) + a(n+3), which is a(n+4) by the tetranacci recurrence.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- This is the program of [A000078](../../A000xxx/A000078/) with the seeds
  1, 3, 7, 15. a(n) is the sum of the n-th powers of the roots of
  x⁴ = x³ + x² + x + 1, the trace of the n-th power of its companion
  matrix (the entry's formula).
- Keeping the leading 4 in the window (`l=4,1,3,7`) saves a byte of seeds
  but `print(l[0])` costs three.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(15087), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 3501 terms (a(1) to a(3501)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001648), CC BY-SA 4.0.
