# A000420

> Powers of 7: a(n) = 7^n.
> — [OEIS A000420](https://oeis.org/A000420)

Offset 0: 1, 7, 49, 343, 2401, 16807, 117649, 823543, 5764801, 40353607, …

### Python 3 — 24 bytes

```python
n=1
while[print(n)]:n*=7
```

**How it works**

- Initially n=1=7⁰. If the current print is 7ᵏ, the body replaces
  n by 7·7ᵏ=7^(k+1), establishing every subsequent term by induction.
- `print(n)` runs while evaluating the condition and returns `None`.
  The one-element list `[None]` is true, so printing also supplies
  the infinite-loop condition.
- The value itself is the whole state: no exponent counter or call
  to `pow` is needed. This is [A000400](../A000400/) with multiplier
  7 instead of 6.

**Notes**

- `n=1` followed by `while 1:print(n);n*=7` is 25 bytes; placing
  the print in a list condition saves one byte.
- Exact integer arithmetic, correct at every index. a(5089)=7^5089
  is the first term with more than 4300 decimal digits, where the
  default integer-to-string limit of Python 3.11+ stops printing.
  This interpreter limit is not counted as a correctness failure.
- There is one multiplication per term and only one stored value,
  although the value's number of digits grows linearly with its index.
- The b-file has 101 terms (indices 0 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 24 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000420), CC BY-SA 4.0.
