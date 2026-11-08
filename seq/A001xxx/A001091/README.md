# A001091

> a(n) = 8*a(n-1) - a(n-2); a(0) = 1, a(1) = 4.
> — [OEIS A001091](https://oeis.org/A001091)

Offset 0: 1, 4, 31, 244, 1921, 15124, 119071, 937444, 7380481, 58106404, …

### Python 3 — 35 bytes

```python
a=b=1
while[print(a)]:a+=3*b;b+=2*a
```

**How it works**

- The recurrence a(n+1) = 8·a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 6·a(n). So the program keeps the first
  difference d(n) = a(n+1) − a(n) instead of the previous term:
  a(n+1) = a(n) + d(n) and d(n+1) = d(n) + 6·a(n+1).
- Every d(n) is a multiple of 3 (d(0) = 4 − 1 = 3, and the steps add
  6·a), so `b` holds d(n)/3: `a+=3*b` steps `a`, then `b+=2*a` uses the
  new `a`. Both start at 1: `a=b=1`.
- Exact integers.

**Notes**

- Here the trick only ties: the tuple form `a,b=1,4` /
  `while[print(a)]:a,b=b,8*b-a`, `a=1;b=3` with `a+=b;b+=6*a`, and the
  [A001090](../A001090/) layout `a=4;b=3` / `while[print(a:=a-b)]:b-=6*a`
  are all 35 bytes. The page keeps the form of its siblings
  [A001081](../A001081/) and [A001085](../A001085/) (T(n, 8) and T(n, 10)).
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, `x=-x-K*y`, either order, K ≤ 24), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter.
- a(n) = T(n, 4) (Chebyshev). With [A001090](../A001090/) (0, 1, 8, …, same
  recurrence) it gives the solutions of x² − 15y² = 1.
- Python's 4300-digit int-to-str limit stops the program at a(4799), the
  first term with 4301 digits, after printing a(0) to a(4798).
- The b-file has 201 terms (a(0) to a(200), 179 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001091), CC BY-SA 4.0.
