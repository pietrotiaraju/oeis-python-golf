# A001085

> a(n) = 20*a(n-1) - a(n-2).
> — [OEIS A001085](https://oeis.org/A001085)

Offset 0: 1, 10, 199, 3970, 79201, 1580050, 31521799, 628855930, 12545596801, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a)]:a+=9*b;b+=2*a
```

**How it works**

- The recurrence a(n+1) = 20·a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 18·a(n). So the program keeps the first
  difference d(n) = a(n+1) − a(n) instead of the previous term:
  a(n+1) = a(n) + d(n) and d(n+1) = d(n) + 18·a(n+1).
- Every d(n) is a multiple of 9 (d(0) = 10 − 1 = 9, and the steps add
  18·a), so `b` holds d(n)/9: `a+=9*b` steps `a`, then `b+=2*a` uses the
  new `a`. Both start at 1: `a=b=1`.
- Two in-place statements replace the tuple swap, and the equal start
  values share one assignment. Exact integers.

**Notes**

- The tuple form `a,b=1,10` / `while[print(a)]:a,b=b,20*b-a` is 37 bytes.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, `x=-x-K*y`, either order, K ≤ 24), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = T(n, 10) (Chebyshev). With [A001084](../A001084/) (0, 3, 60, …,
  same recurrence) it gives the solutions of x² − 11y² = 1;
  [A001081](../A001081/) and [A001091](../A001091/) are the same program
  for T(n, 8) and T(n, 4).
- Python's 4300-digit int-to-str limit stops the program at a(3309), the
  first term with more than 4300 digits, after printing a(0) to a(3308).
- The b-file has 201 terms (a(0) to a(200), 260 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001085), CC BY-SA 4.0.
