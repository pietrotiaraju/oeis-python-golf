# A001608

> Perrin sequence (or Perrin numbers, or Ondrej Such sequence): a(n) = a(n-2) + a(n-3) with a(0) = 3, a(1) = 0, a(2) = 2.
> — [OEIS A001608](https://oeis.org/A001608)

Offset 0: 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, 51, 68, 90, 119, …

### Python 3 — 41 bytes

```python
a,b,c=3,0,2
while[print(a)]:a,b,c=b,c,a+b
```

**How it works**

- (a, b, c) holds three consecutive terms (a(t), a(t+1), a(t+2)); the
  tuple shift `a,b,c=b,c,a+b` appends a(t+3) = a(t+1) + a(t). The start
  is the data's a(0), a(1), a(2) = 3, 0, 2. This is the program of the
  Padovan sequence [A000931](../../A000xxx/A000931/) with Perrin's seeds.

**Notes**

- a(n) is the sum of the n-th powers of the three roots of x³ = x + 1.
- A search over three-variable tuples with short entries (in other
  coordinates and with any variable or a sum of two printed) found nothing shorter. Chains of three in-place statements
  with coefficients ±1 allow starts with two equal values, but the best is
  42 bytes (`a=b=3;c=1` / `while[print(b)]:b=a-b;c=b-c;a+=c`).
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 8173 terms (a(0) to a(8172)); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001608), CC BY-SA 4.0.
