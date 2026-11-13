# A001639

> A Fielder sequence. a(n) = a(n-1) + a(n-3) + a(n-4) + a(n-5), n >= 6.
> — [OEIS A001639](https://oeis.org/A001639)

Offset 1: 1, 1, 4, 9, 16, 22, 36, 65, 112, 186, 309, 522, 885, 1492, 2509, …

### Python 3 — 49 bytes

```python
l=1,1,4,9,16
while 1:a,*l=*l,sum(l)-l[3];print(a)
```

**How it works**

- `l` holds 5 consecutive terms, a(n) to a(n+4), starting from the
  data's a(1) to a(5) = 1, 1, 4, 9, 16.
- `*l,sum(l)-l[3]` builds the 6 terms a(n) to a(n+5): the old 5 and
  `sum(l)-l[3]` = a(n) + a(n+1) + a(n+2) + a(n+4), which is a(n+5) by the recurrence a(n+5) = a(n+4) + a(n+2) + a(n+1) + a(n).
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 5, a(n+1) to a(n+5), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(1).
- Integers are exact, so every term is right, for every n.

**Notes**

- The g.f. x(1 + 3x² + 4x³ + 5x⁴)/(1 − x − x³ − x⁴ − x⁵) has numerator
  −xD′(x), so a(n) is the sum of the n-th powers of the roots of
  x⁵ = x⁴ + x² + x + 1 (a Fielder sequence; the seeds are Newton's
  identities). The program does not need this.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(18973), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1000 terms (a(1) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001639), CC BY-SA 4.0.
