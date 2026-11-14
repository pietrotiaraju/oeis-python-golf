# A001737

> Squares written in base 2.
> — [OEIS A001737](https://oeis.org/A001737)

Offset 0: 0, 1, 100, 1001, 10000, 11001, 100100, 110001, 1000000, 1010001, …

### Python 3 — 33 bytes

```python
n=0
while[print(f"{n*n:b}")]:n+=1
```

**How it works**

- The format spec `b` writes an integer in binary without the `0b` prefix,
  so `f"{n*n:b}"` is n² in base 2 (and `0` for n = 0).
- `while[print(…)]:` is always true (the list `[None]` is not empty), and
  `n+=1` moves on.

**Notes**

- `bin(n*n)[2:]` is 2 bytes longer. Python's format specs only know bases 2,
  8 and 16, so the other bases of this family ([A001738](../A001738/) to
  [A001741](../A001741/)) need a conversion of their own.
- Exact, correct for every n. The b-file has 1001 terms (n = 0 to 1000); the
  bar is the whole b-file, printed in a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001737), CC BY-SA 4.0.
