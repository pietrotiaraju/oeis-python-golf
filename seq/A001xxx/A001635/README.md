# A001635

> A Fielder sequence: a(n) = a(n-1) + a(n-2) - a(n-6), n >= 7.
> — [OEIS A001635](https://oeis.org/A001635)

Offset 1: 0, 2, 3, 6, 10, 11, 21, 30, 48, 72, 110, 171, 260, 401, 613, 942, …

### Python 3 — 48 bytes

```python
l=0,2,3,6,10
while 1:a,*l=*l,sum(l[:4]);print(a)
```

**How it works**

- The title's recurrence a(n) = a(n−1) + a(n−2) − a(n−6), n ≥ 7, is
  equivalent to the shorter one in the entry's formula section,
  a(n) = a(n−2) + a(n−3) + a(n−4) + a(n−5) for n ≥ 6. Put
  r(n) = a(n) − a(n−2) − a(n−3) − a(n−4) − a(n−5); the sums telescope to
  r(n) − r(n−1) = a(n) − a(n−1) − a(n−2) + a(n−6), so the title says that
  r(n) = r(n−1) for n ≥ 7, and r(6) = 11 − 6 − 3 − 2 − 0 = 0 from the data.
  So r(n) = 0 for every n ≥ 6. (In polynomials: x⁶ − x⁵ − x⁴ + 1 =
  (x − 1)(x⁵ − x³ − x² − x − 1).)
- `l` holds 5 consecutive terms, a(n) to a(n+4), starting from the
  data's a(1) to a(5) = 0, 2, 3, 6, 10.
- `*l,sum(l[:4])` builds the 6 terms a(n) to a(n+5): the old 5 and
  `sum(l[:4])` = a(n) + a(n+1) + a(n+2) + a(n+3), which is a(n+5) by the recurrence above.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 5, a(n+1) to a(n+5), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The g.f. x²(2 + x + x² + x³ − 5x⁴)/(1 − x − x² + x⁶) reduces to
  x(2x + 3x² + 4x³ + 5x⁴)/(1 − x² − x³ − x⁴ − x⁵) = −xD′(x)/D(x), so a(n) is
  the sum of the n-th powers of the roots of x⁵ = x³ + x² + x + 1, as for
  every Fielder sequence (the seeds are Newton's identities). The program
  does not need this.
- The title's order-6 recurrence needs six seeds and `sum(l[4:])-l[0]`:
  `l=0,2,3,6,10,11` / `while 1:a,*l=*l,sum(l[4:])-l[0];print(a)` is 56 bytes.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(23134), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001635), CC BY-SA 4.0.
