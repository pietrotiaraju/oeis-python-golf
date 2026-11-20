# A001945

> a(n+6) = -a(n+5) + a(n+4) + 3a(n+3) + a(n+2) - a(n+1) - a(n). a(n) = sign(n) if abs(n)<=3.
> — [OEIS A001945](https://oeis.org/A001945)

Offset 0: 0, 1, 1, 1, 5, 1, 7, 8, 5, 19, 11, 23, 35, 27, 64, 61, 85, 137, 133, 229, 275, …

### Python 3 — 63 bytes

```python
a,b,c=d,e,f=3,0,2
while[print(a-d)]:a,b,c,d,e,f=b,c,a+b,f-d,d,e
```

**How it works**

- **Factor the recurrence.** Its characteristic polynomial is
  x⁶ + x⁵ − x⁴ − 3x³ − x² + x + 1 = (x³ − x − 1)(x³ + x² − 1). The roots α,
  β, γ of x³ − x − 1 have product 1, and the roots of x³ + x² − 1 are their
  reciprocals.
- **Perrin both ways.** The Perrin numbers P(n) = αⁿ + βⁿ + γⁿ
  ([A001608](../A001608/)) satisfy P(n + 3) = P(n + 1) + P(n) for all
  integers n, and P(−n) = α⁻ⁿ + β⁻ⁿ + γ⁻ⁿ. So P(n) − P(−n) satisfies the
  sixth-order recurrence. It is odd in n, and P(1) − P(−1) = 0 + 1,
  P(2) − P(−2) = 2 − 1, P(3) − P(−3) = 3 − 2 are all 1, so it equals sign(n)
  for |n| ≤ 3, and a(n) = P(n) − P(−n) for every n. (This is Peter Bala's
  (αⁿ − 1)(βⁿ − 1)(γⁿ − 1) from the entry, multiplied out with αβγ = 1.)
- **Program.** (a, b, c) = (P(n), P(n + 1), P(n + 2)) steps forward with
  P(n + 3) = P(n + 1) + P(n), and (d, e, f) = (P(−n), P(1 − n), P(2 − n))
  steps backward with P(−n − 1) = P(2 − n) − P(−n), the same recurrence
  solved for its lowest term. Both triples start at P(0), P(1), P(2) =
  3, 0, 2, so one chained assignment sets them, and each pass prints a − d.

**Notes**

- The recurrence itself from a(0), …, a(5) = 0, 1, 1, 1, 5, 1 in a list is
  73 bytes; a six-variable state form fed with the numerator coefficients
  is 76.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 63 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001945), CC BY-SA 4.0.
