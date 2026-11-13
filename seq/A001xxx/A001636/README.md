# A001636

> A Fielder sequence: a(n) = a(n-1) + a(n-2) - a(n-7), n >= 8.
> — [OEIS A001636](https://oeis.org/A001636)

Offset 1: 0, 2, 3, 6, 10, 17, 21, 38, 57, 92, 143, 225, 351, 555, 868, 1366, …

### Python 3 — 51 bytes

```python
l=0,2,3,6,10,17
while 1:a,*l=*l,sum(l[:5]);print(a)
```

**How it works**

- The title's recurrence a(n) = a(n−1) + a(n−2) − a(n−7), n ≥ 8, is
  equivalent to the one in the entry's formula section,
  a(n) = a(n−2) + a(n−3) + a(n−4) + a(n−5) + a(n−6) for n ≥ 7. Put
  r(n) = a(n) − a(n−2) − … − a(n−6); the sums telescope to
  r(n) − r(n−1) = a(n) − a(n−1) − a(n−2) + a(n−7), so the title says that
  r(n) = r(n−1) for n ≥ 8, and r(7) = 21 − 10 − 6 − 3 − 2 − 0 = 0 from the
  data. So r(n) = 0 for every n ≥ 7. (In polynomials: x⁷ − x⁶ − x⁵ + 1 =
  (x − 1)(x⁶ − x⁴ − x³ − x² − x − 1).)
- `l` holds 6 consecutive terms, a(n) to a(n+5), starting from the
  data's a(1) to a(6) = 0, 2, 3, 6, 10, 17.
- `*l,sum(l[:5])` builds the 7 terms a(n) to a(n+6): the old 6 and
  `sum(l[:5])` = a(n) + a(n+1) + … + a(n+4), which is a(n+6) by the recurrence above.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 6, a(n+1) to a(n+6), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The g.f. x²(2 + x + x² + x³ + x⁴ − 6x⁵)/(1 − x − x² + x⁷) reduces to
  −xD′(x)/D(x) with D = 1 − x² − x³ − x⁴ − x⁵ − x⁶, so a(n) is the sum of
  the n-th powers of the roots of x⁶ = x⁴ + x³ + x² + x + 1 (a Fielder
  sequence; the seeds are Newton's identities). The polynomial factors as
  (x + 1)(x⁵ − x⁴ − x² − 1). The program does not need this.
- The program spells out its six seeds, the data's a(1) to a(6), so it
  went through a review. They are fixed by the entry: the first six
  coefficients of its g.f. (Newton's identities for the power sums), and
  every later term follows from the recurrence above.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(21945), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001636), CC BY-SA 4.0.
