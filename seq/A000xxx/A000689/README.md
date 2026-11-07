# A000689

> Final decimal digit of 2^n.
> — [OEIS A000689](https://oeis.org/A000689)

Offset 0: 1, 2, 4, 8, 6, 2, 4, 8, 6, 2, 4, 8, 6, 2, 4, …

### Python 3 — 27 bytes

```python
n=1
while[print(n)]:n=n%5*2
```

**How it works**

- The last digit of 2^(k+1) is 2·d mod 10, where d is the last digit of 2^k.
  For every integer d, 2d mod 10 = 2·(d mod 5) (the two differ by
  10·⌊d/5⌋), and `n%5*2` is one byte under `n*2%10`.
- So n runs through 1, 2, 4, 8, 6, 2, 4, 8, 6, … and is printed as it goes.

**Notes**

- Exact and constant time per term, so every term is right.
- Same length: `print(n%10)` with `n*=2` (27 bytes), but there n grows
  without bound.
- The b-file has 81 terms; the bar is all 81, printed instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000689), CC BY-SA 4.0.
