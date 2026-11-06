# A000384

> Hexagonal numbers: a(n) = n*(2*n-1).
> — [OEIS A000384](https://oeis.org/A000384)

Offset 0: 0, 1, 6, 15, 28, 45, 66, 91, 120, 153, 190, 231, 276, 325, …

### Python 3 — 29 bytes

```python
m=1
while[print(m*m>>3)]:m-=4
```

**How it works**

- The completed-square trick of the triangular numbers
  [A000217](../A000217/): for odd m, m² ≡ 1 (mod 8), so `m*m>>3` is exactly
  (m² − 1)/8.
- With m = 1 − 4n this is ((4n − 1)² − 1)/8 = (16n² − 8n)/8 = n(2n − 1). The
  hexagonal numbers are the triangular numbers T(−2n) = T(2n − 1), and
  m = 2(−2n) + 1 is the odd number the triangular trick needs.
- m runs 1, −3, −7, …; counting down from 1 instead of up from −1 saves the
  minus sign in the start value.

**Notes**

- The closed form, `n=0` + `while[print(2*n*n-n)]:n+=1`, is 30 bytes, and
  `n*(2*n-1)` is 2 bytes longer than that. Summing the differences 4n + 1,
  `a=0;d=1` + `while[print(a)]:a+=d;d+=4`, is 33.
- A search over every expression of up to 5 bytes in m over the characters
  `m0123456789+-*/%&|^~<>()` (147,257 valid ones of 5 bytes), with start
  values 0 to 9 and steps ±1 to ±9, found none that prints a(0) … a(7), so
  this frame cannot get to 28 bytes. Without bit tricks the reason is simple:
  with an integer step t, `m*m`, `m*-~m` and `m*~-m` have leading coefficient
  t², never 2.
- Exact integers, so every term is right; the int-to-str limit would only be
  reached near n = 10^2150.
- The b-file has 10001 terms (n = 0 to 10000) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000384), CC BY-SA 4.0.
