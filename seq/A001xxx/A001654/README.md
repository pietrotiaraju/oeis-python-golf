# A001654

> Golden rectangle numbers: F(n) * F(n+1), where F(n) = A000045(n) (Fibonacci numbers).
> — [OEIS A001654](https://oeis.org/A001654)

Offset 0: 0, 1, 2, 6, 15, 40, 104, 273, 714, 1870, 4895, 12816, 33552, 87841, …

### Python 3 — 35 bytes

```python
a=0;b=1
while[print(a*b)]:a,b=b,a+b
```

**How it works**

- `a`, `b` are the Fibonacci pair F(n), F(n+1); each pass prints their
  product and steps the pair.

**Notes**

- Folding the step into the print (`print(b*(b:=a+b))` then `a=b-a`, the
  trick of [A001655](../A001655/)) is 38 bytes here: with only two factors
  there is nothing to save.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001654), CC BY-SA 4.0.
