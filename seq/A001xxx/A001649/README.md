# A001649

> A Fielder sequence.
> — [OEIS A001649](https://oeis.org/A001649)

Offset 1: 1, 3, 7, 15, 26, 57, 106, 207, 403, 788, 1530, 2985, 5812, 11322, …

### Python 3 — 53 bytes

```python
l=1,3,7,15,26,57
while 1:a,*l=*l,sum(l)-l[1];print(a)
```

**How it works**

- The name gives no rule; the entry's g.f.
  x(1 + 2x + 3x² + 4x³ + 6x⁵)/(1 − x − x² − x³ − x⁴ − x⁶) has a numerator of
  degree 6, so a(n) = a(n−1) + a(n−2) + a(n−3) + a(n−4) + a(n−6) for n ≥ 7,
  from a(1), …, a(6) = 1, 3, 7, 15, 26, 57.
- `l` holds 6 consecutive terms, a(n) to a(n+5), starting from the
  data's a(1) to a(6) = 1, 3, 7, 15, 26, 57.
- `*l,sum(l)-l[1]` builds the 7 terms a(n) to a(n+6): the old 6 and
  `sum(l)-l[1]` = a(n) + a(n+2) + a(n+3) + a(n+4) + a(n+5), which is a(n+6) by the recurrence above.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 6, a(n+1) to a(n+6), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The numerator is −xD′(x), so a(n) is the sum of the n-th powers of the
  roots of x⁶ = x⁵ + x⁴ + x³ + x² + 1 (the polynomial factors as
  (x + 1)(x⁵ − 2x⁴ + x³ − 2x² + x − 1)). The program does not need this.
- The program spells out its six seeds, the data's a(1) to a(6), so it
  went through a review. They are fixed by the entry: the first six
  coefficients of its g.f. (Newton's identities for the power sums), and
  every later term follows from the recurrence above.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(14849), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001649), CC BY-SA 4.0.
