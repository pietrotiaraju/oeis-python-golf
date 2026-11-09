# A001344

> a(n) = Sum_{k=0..2} (n+k)! * C(2,k).
> — [OEIS A001344](https://oeis.org/A001344)

Offset -1: 2, 5, 11, 38, 174, 984, 6600, 51120, 448560, 4394880, …

For n ≥ 0, a(n) = n! + 2·(n+1)! + (n+2)! = n!·(n² + 5n + 5). At n = −1 the
k = 0 term would be (−1)!, so the sum does not define a(−1); the OEIS gives
a(−1) = 2 (Karttunen's formula on the entry).

### Python 3 — 49 bytes

```python
f=2;n=0
while[print(f*n*(n+3)+f)]:f=f*n or 1;n+=1
```

**How it works**

- The loop counter `n` is j = n + 1 (it starts at 0 for a(−1)). For j ≥ 1,
  a(j−1) = (j−1)!·((j−1)² + 5(j−1) + 5) = (j−1)!·(j² + 3j + 1)
  = (j−1)! + j!·(j + 3), and with `f` = (j−1)! that is `f*n*(n+3)+f`.
- `f` starts at 2, so at j = 0 the print gives 0 + 2 = 2 = a(−1). Then
  `f=f*n or 1` turns 2·0 = 0 into 1 = 0!; from j = 1 on f·j is never 0, so
  the same statement is `f*=n` and f = (j−1)! at every later print.
- The value 2 is the only stored term. It is what the sum gives if (−1)! is
  read as −1 (−1 + 2·0! + 1! = 2), the same reading that gives a(−1) = 7,
  23, 88 in [A001345](../A001345/), [A001346](../A001346/) and
  [A001347](../A001347/).
- `print` returns `None` and `[None]` is truthy, so the loop never ends.
  Exact integers, so every term is right.

**Notes**

- Printing a(−1) separately (`f=n=1;print(2)` and `f*=n`) is 50 bytes.
  Computing a(−1) from (−1)! = −1 instead of storing it, as in
  [A001346](../A001346/), is 50 (`g=1;x=3` /
  `while[print(g*x+g//(x-3or-1))]:x+=1;g*=x-3`), or 51 with (j−1)! and j!
  in two variables (`f=-1;g=1;n=0` /
  `while[print(f+g*(n+3))]:n+=1;f,g=g,g*n`).
  `f*(n*n+3*n+1)` is 2 bytes longer than `f*n*(n+3)+f`.
- Python's 4300-digit int-to-str limit stops the program at a(1557), the
  first term with more than 4300 digits, after printing a(−1) to a(1556).
- The b-file has 102 terms (n = −1 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001344), CC BY-SA 4.0.
