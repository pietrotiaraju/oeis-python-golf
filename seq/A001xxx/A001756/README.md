# A001756

> a(n) = A059366(n,n-3) = A059366(n,3) for n >= 3, where the triangle A059366 arises from the expansion of a trigonometric integral.
> — [OEIS A001756](https://oeis.org/A001756)

Offset 3: 15, 60, 450, 4500, 55125, 793800, 13097700, 243243000, 5016886875, 113716102500, …

### Python 3 — 46 bytes

```python
a=15;i=0
while[print(a)]:i+=2;a=a*~-i*(i+6)//i
```

**How it works**

- The triangle A059366 has the closed form
  T(n, k) = C(2k, k)·C(2n−2k, n−k)·n!/2ⁿ (the entry's formula
  a(n) = 20·C(2n−6, n−3)·n!/2ⁿ is its k = 3 column, and the
  binomial(−1/2, ·) formula is the same thing). So a(3) = 15 and, from
  C(2m, m)/C(2m−2, m−1) = 2(2m−1)/m with m = n − 3,
  a(n) = a(n−1)·n(2n−7)/(n−3), Deléham's recurrence in the entry.
- With i = 2(n−3): 2n − 7 = i − 1 and n/(n−3) = (i+6)/i, so each pass does
  `i+=2;a=a*~-i*(i+6)//i`. The quotient is the integer a(n), so the floor
  division is exact.

**Notes**

- Exact integer arithmetic, correct for every n. a(1424) is the first term
  over 4300 digits, where Python's int-to-str limit stops the program.
- Counting n itself, `a=15;n=3` / `…n+=1;a=a*n*(2*n-7)//(n-3)`, is 50 bytes.
- The b-file has 98 terms (a(3) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly. The central column is
  [A001757](../A001757/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 46 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001756), CC BY-SA 4.0.
