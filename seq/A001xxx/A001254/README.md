# A001254

> Squares of Lucas numbers.
> — [OEIS A001254](https://oeis.org/A001254)

Offset 0: 4, 1, 9, 16, 49, 121, 324, 841, 2209, 5776, 15129, 39601, 103684, 271441, 710649, 1860496, 4870849, 12752041, …

### Python 3 — 35 bytes

```python
a,b=2,1
while[print(a*a)]:a,b=b,a+b
```

**How it works**

- `a,b` walk the Lucas numbers 2, 1, 3, 4, 7, …, and each one is printed
  squared.

**Notes**

- The whole b-file (2376 terms) prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001254), CC BY-SA 4.0.
