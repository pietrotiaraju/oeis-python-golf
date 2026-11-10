# A001517

> Bessel polynomials y_n(x) (see A001498) evaluated at 2.
> — [OEIS A001517](https://oeis.org/A001517)

Offset 0: 1, 3, 19, 193, 2721, 49171, 1084483, 28245729, 848456353, …

### Python 3 — 42 bytes

```python
a=b=1;k=2
while[print(b)]:a,b=b,k*b+a;k+=4
```

**How it works**

- The Bessel polynomials satisfy **y_n(x) = (2n−1)·x·y_{n−1}(x) + y_{n−2}(x)**
  with y_0 = 1, y_1 = 1 + x (Krall and Frink, 1949; Grosswald, *Bessel
  Polynomials*, 1978; coefficients in [A001498](../A001498/)). At x = 2:
  a(n) = (4n−2)·a(n−1) + a(n−2).
- As in [A001515](../A001515/), the recurrence run backwards gives
  y_{−1} = 1, so `a=b=1` is the pair (y_{−1}, y_0) and no step is special.
  `k` is the multiplier (2n−1)·2 of the next step: it starts at 2 and
  grows by 4.
- `while[print(b)]:` prints in the loop condition, `a,b=b,k*b+a` steps.

**Notes**

- Starting `a=b=k=1` and writing `2*k*b` is the same length.
- Exact integer arithmetic, so the program is right for every n; the first
  term over the 4300-digit int-to-str limit is a(1309).
- The b-file has 335 terms (n = 0 to 334); they all print in well under a
  second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001517), CC BY-SA 4.0.
