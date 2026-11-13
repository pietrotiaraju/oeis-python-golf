# A001623

> Number of 3 X n reduced (normalized) Latin rectangles.
> — [OEIS A001623](https://oeis.org/A001623)

Offset 3: 1, 4, 46, 1064, 35792, 1673792, 103443808, 8154999232, …

### Python 3 — 93 bytes

```python
a=b=0;c=f=2;n=3
while f:=2**n*~-n-n*f:a,b,c=n*(n*a+b+2*c)-f,n*a,n*b;print(a//~-n//(n-2));n+=1
```

**How it works**

- The entry's comment: a k × n Latin rectangle is normalized when its
  first row is 0, 1, …, n−1 and reduced when also its first column is
  0, 1, …, k−1, and L = n!·N = (n!(n−1)!/(n−k)!)·R. So for k = 3,
  **a(n) = N/((n−1)(n−2))** with N = [A000186](../../A000xxx/A000186/)(n),
  the 3 × n rectangles with the first row in order. (Relabelling the
  symbols by a permutation that fixes 0 and then reordering the columns
  to restore the first row maps the normalized rectangles with first
  column (0, x, y) one-to-one onto those with any other first column
  (0, x′, y′), so each of the (n−1)(n−2) first columns occurs equally
  often.)
- The loop is the A000186 program: from Gessel's e.g.f. it derives
  u(n) = n·u(n−1) + u(n−2) + 2u(n−3) + E(n) for u(n) = N(n)/n!, and at
  the top of the pass for n keeps `a` = N(n−1), `b` = (n−1)·N(n−2),
  `c` = (n−1)(n−2)·N(n−3) and the correction `f`, so
  N(n) = n(n·a + b + 2c) − f (see that page).
- Instead of zero seeds at n = 0 the loop starts at n = 3 with the state
  A000186 reaches there: a = N(2) = 0, b = 0, c = 2, f = 2. That is 4
  bytes more than `a=b=c=f=n=0` but saves the guard
  `n>2and` that would skip n = 0, 1, 2, where (n−1)(n−2) is 0.
- `a//~-n//(n-2)` divides by n−1 and then by n−2; both divisions are
  exact, since (n−1)(n−2) divides N(n).

**Notes**

- Exact integer arithmetic, so the program is right for every n. The
  loop condition never stops it: A000186's page shows f is never
  divisible by 3.
- The whole b-file (252 terms, up to a(254)) prints in well under a
  second; the bar is the whole b-file in 60 s.
- a(861) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 93 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001623), CC BY-SA 4.0.
