# A000369

> Triangle of numbers related to triangle A049213; generalization of Stirling numbers of second kind A008277, Bessel triangle A001497.
> — [OEIS A000369](https://oeis.org/A000369)

Offset 1: 1, 3, 1, 21, 9, 1, 231, 111, 18, 1, 3465, 1785, 345, 30, 1, …

The triangle is read by rows, a(n, m) for n ≥ 1 and m = 1 … n, so the
program prints row 1, then row 2, and so on, one entry per line.

### Python 3 — 76 bytes

```python
*r,p=1,
while[*map(print,r),k:=4*len(r)]:r=[p+(p:=x)*(k:=k-1)for x in r+[0]]
```

**How it works**

- The OEIS recurrence: a(n+1, m) = (4n − m)·a(n, m) + a(n, m−1), with
  a(n, 0) = 0 and a(n, m) = 0 for m > n.
- `r` is the current row n, so n = len(r). The header prints it and sets
  k = 4n; the walrus sits in the list display, which is non-empty, so the
  loop never stops.
- The comprehension walks r + [0], that is a(n, 1), …, a(n, n), a(n, n+1) = 0.
  For the entry x = a(n, m), `p` still holds the previous entry a(n, m−1),
  and `p+(p:=x)*(k:=k-1)` reads that old p before storing x, while k counts
  down to 4n − m. That is a(n+1, m).
- The last entry walked is the padding 0, so p is 0 again at the start of
  every row and needs no reset.
- The loop starts one row early: `*r,p=1,` sets r = [] (row 0) and p = 1.
  The first pass prints nothing, and the comprehension over [0] gives
  [p + 0] = [1], row 1. That is a byte under `r=[1];p=0`.

**Notes**

- Exact integer arithmetic, correct for every row. The b-file has
  1275 terms (rows 1 to 50) and all of them print at once; only the
  4300-digit int-to-str limit of Python 3.11+ stops the program, far
  beyond it. The bar is the whole b-file in 60 s.
- Pairing the entries with `zip(r+[0],[0]+r)` and `x*(k:=k-1)+y` is
  7 bytes longer, and resetting `p:=0` in the header instead of the early
  start costs a byte more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 76 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000369), CC BY-SA 4.0.
