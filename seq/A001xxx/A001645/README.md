# A001645

> A Fielder sequence.
> — [OEIS A001645](https://oeis.org/A001645)

Offset 1: 1, 3, 7, 11, 26, 45, 85, 163, 304, 578, 1090, 2057, 3888, 7339, …

### Python 3 — 50 bytes

```python
l=1,3,7,11,26
while 1:a,*l=*l,sum(l)-l[1];print(a)
```

**How it works**

- The name gives no rule; the entry's g.f.
  x(1 + 2x + 3x² + 5x⁴)/(1 − x − x² − x³ − x⁵) has a numerator of degree 5,
  so a(n) = a(n−1) + a(n−2) + a(n−3) + a(n−5) for n ≥ 6, from
  a(1), …, a(5) = 1, 3, 7, 11, 26.
- `l` holds 5 consecutive terms, a(n) to a(n+4), starting from the
  data's a(1) to a(5) = 1, 3, 7, 11, 26.
- `*l,sum(l)-l[1]` builds the 6 terms a(n) to a(n+5): the old 5 and
  `sum(l)-l[1]` = a(n) + a(n+2) + a(n+3) + a(n+4), which is a(n+5) by the recurrence above.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 5, a(n+1) to a(n+5), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The numerator is −xD′(x), so a(n) is the sum of the n-th powers of the
  roots of x⁵ = x⁴ + x³ + x² + 1, the trace of the n-th power of its
  companion matrix (the entry's formula). The program does not need this.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(15572), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001645), CC BY-SA 4.0.
