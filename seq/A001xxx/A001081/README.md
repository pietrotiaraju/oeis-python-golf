# A001081

> a(n) = 16*a(n-1) - a(n-2).
> — [OEIS A001081](https://oeis.org/A001081)

Offset 0: 1, 8, 127, 2024, 32257, 514088, 8193151, 130576328, 2081028097, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a)]:a+=7*b;b+=2*a
```

**How it works**

- The recurrence a(n+1) = 16·a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 14·a(n). So the program keeps the first
  difference d(n) = a(n+1) − a(n) instead of the previous term:
  a(n+1) = a(n) + d(n) and d(n+1) = d(n) + 14·a(n+1).
- Every d(n) is a multiple of 7 (d(0) = 8 − 1 = 7, and the steps add
  14·a), so `b` holds d(n)/7: `a+=7*b` steps `a`, then `b+=2*a` uses the
  new `a`. Both start at 1: `a=b=1`.
- Two in-place statements replace the tuple swap, and the equal start
  values share one assignment. Exact integers.

**Notes**

- The tuple form `a,b=1,8` / `while[print(a)]:a,b=b,16*b-a` is 36 bytes.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, `x=-x-K*y`, either order, K ≤ 24), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = T(n, 8) (Chebyshev). With [A001080](https://oeis.org/A001080)
  (0, 3, 48, …, same recurrence) it gives the solutions of x² − 7y² = 1;
  [A001085](../A001085/) and [A001091](../A001091/) are the same program
  for T(n, 10) and T(n, 4).
- Python's 4300-digit int-to-str limit stops the program at a(3577), the
  first term with 4301 digits, after printing a(0) to a(3576).
- The b-file has 201 terms (a(0) to a(200), 241 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001081), CC BY-SA 4.0.
