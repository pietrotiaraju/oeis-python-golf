# A001068

> a(n) = floor(5*n/4), numbers that are congruent to {0, 1, 2, 3} mod 5.
> — [OEIS A001068](https://oeis.org/A001068)

Offset 0: 0, 1, 2, 3, 5, 6, 7, 8, 10, 11, …

### Python 3 — 27 bytes

```python
n=0
while[print(n>>2)]:n+=5
```

**How it works**

- n runs over the multiples of 5 (0, 5, 10, …), so at index k it is 5k and
  `n>>2` is ⌊5k/4⌋: shifting right by 2 is floor division by 4.
- Stepping by 5 removes the multiplication from the print; the index itself
  is never stored.

**Notes**

- A plain counter, `while[print(n*5>>2)]:n+=1`, is 29 bytes; filtering the
  integers not ≡ 4 (mod 5) (the other description in the name) costs more.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 10001 terms (up to a(10000)); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001068), CC BY-SA 4.0.
