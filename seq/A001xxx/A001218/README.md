# A001218

> a(n) = 3^n mod 100.
> — [OEIS A001218](https://oeis.org/A001218)

Offset 0: 1, 3, 9, 27, 81, 43, 29, 87, 61, 83, 49, 47, 41, 23, 69, 7, 21, 63, 89, 67, 1, …

### Python 3 — 29 bytes

```python
n=1
while[print(n)]:n=n*3%100
```

**How it works**

- Keep only the residue: 3ⁿ⁺¹ mod 100 = 3·(3ⁿ mod 100) mod 100, so
  `n=n*3%100` steps through the period-20 cycle.

**Notes**

- The whole b-file prints at once.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001218), CC BY-SA 4.0.
