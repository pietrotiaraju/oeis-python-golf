# A001809

> a(n) = n! * n(n-1)/4.
> — [OEIS A001809](https://oeis.org/A001809)

Offset 0: 0, 0, 1, 9, 72, 600, 5400, 52920, 564480, 6531840, 81648000, 1097712000, …

### Python 3 — 42 bytes

```python
f=1;n=0
while[print(f*n*~-n>>2)]:n+=1;f*=n
```

**How it works**

- a(n) = n!·n(n − 1)/4 is the total number of inversions over all
  permutations of [n]: each of the C(n, 2) pairs is inverted in exactly
  half of the n! permutations.
- `f` is n! (it starts at 0! = 1 and is multiplied by each new n), and
  `f*n*~-n>>2` is n!·n(n − 1)/4 (`~-n` is n − 1; the shift binds after
  the products).
- The shift is an exact division: for n ≥ 2 both n(n − 1) and n! are
  even, so the product is a multiple of 4, and for n = 0, 1 it is 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- [A001804](../A001804/) = 2a(n) starts at n = 2 with `f` = n!/2 and saves
  the shift, but here the offset is 0 and n!/2 is not an integer at
  n = 0, 1. The ratio a(n) = a(n − 1)·n²/(n − 2) cannot start from the
  zero terms a(0) = a(1) = 0.
- Same length with the counter one behind and f = −(n + 1)!, the start
  that saves 2 bytes in [A001810](../A001810/): `f=n=-1` /
  `while[print(f*n*~n>>2)]:n+=1;f*=n+1`.
- a(1557) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001809), CC BY-SA 4.0.
