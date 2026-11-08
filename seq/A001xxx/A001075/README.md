# A001075

> a(0) = 1, a(1) = 2, a(n) = 4*a(n-1) - a(n-2).
> — [OEIS A001075](https://oeis.org/A001075)

Offset 0: 1, 2, 7, 26, 97, 362, 1351, 5042, 18817, 70226, 262087, 978122, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(a)]:a+=b;b+=2*a
```

**How it works**

- The recurrence a(n+1) = 4a(n) − a(n−1) says that the second difference
  is a(n+1) − 2a(n) + a(n−1) = 2a(n). So the program keeps the first
  difference d(n) = a(n+1) − a(n) instead of the previous term:
  a(n+1) = a(n) + d(n) and d(n+1) = d(n) + 2a(n+1).
- `a+=b` steps `a`, then `b+=2*a` uses the new `a`. The start is
  a(0) = 1 and d(0) = 2 − 1 = 1, so both are 1: `a=b=1`.
- Two in-place statements replace the tuple swap, and the equal start
  values share one assignment. Exact integers.

**Notes**

- The tuple form `a,b=1,2` / `while[print(a)]:a,b=b,4*b-a` is 35 bytes.
- An exhaustive search over two-statement updates (`x+=K*y`, `x-=K*y`,
  `x=K*y-x`, …, either order, |K| ≤ 20), the tuple form, and the same
  with a walrus in the print, with the start values solved exactly from
  the first two terms, found nothing shorter; `b-=2*a;a-=b` with `a=b=1` is
  the same length.
- a(n) = T(n, 2) (Chebyshev), and (2 + √3)ⁿ = a(n) + u(n)·√3 with
  u = [A001353](https://oeis.org/A001353); the differences in `b` are
  1, 5, 19, 71, … ([A001834](https://oeis.org/A001834)).
  [A001091](../A001091/), [A001079](../A001079/) and
  [A001081](../A001081/) are the same program for T(n, 4), T(n, 5) and
  T(n, 8), with the difference divided by 3, 4 and 7.
- Python's 4300-digit int-to-str limit stops the program at a(7519), the
  first term with 4301 digits, after printing a(0) to a(7518).
- The b-file has 1746 terms (a(0) to a(1745), 998 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001075), CC BY-SA 4.0.
