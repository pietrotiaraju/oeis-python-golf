# A001810

> a(n) = n!*n*(n-1)*(n-2)/36.
> — [OEIS A001810](https://oeis.org/A001810)

Offset 0: 0, 0, 0, 1, 16, 200, 2400, 29400, 376320, 5080320, 72576000, 1097712000, …

### Python 3 — 49 bytes

```python
f=1;n=0
while[print(f*n*~-n*(n-2)//36)]:n+=1;f*=n
```

**How it works**

- a(n) = n!·n(n − 1)(n − 2)/36 = n!·C(n, 3)/6 is the total number of
  321 patterns over all permutations of [n]: each of the C(n, 3) triples
  is decreasing in one sixth of the n! permutations. So it is an integer
  for every n.
- `f` is n! (it starts at 0! = 1 and is multiplied by each new n), and
  `f*n*~-n*(n-2)//36` is that product over 36 (`~-n` is n − 1). The
  product is exactly 36·a(n), so the floor division is exact; for
  n = 0, 1, 2 it is 0.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- Same length with the cubic m³ − m = (m + 1)m(m − 1), m = n − 1:
  `f=1;m=-1` / `while[print(f*(m**3-m)//36)]:m+=1;f*=m+1`.
- The ratio a(n) = a(n − 1)·n²/(n − 3) that gives [A001805](../A001805/)
  = 6a(n) in 43 bytes cannot start from the zero terms a(0..2).
- a(1556) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001810), CC BY-SA 4.0.
