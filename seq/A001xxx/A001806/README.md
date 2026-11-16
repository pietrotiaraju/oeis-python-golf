# A001806

> a(n) = n! * binomial(n,4).
> — [OEIS A001806](https://oeis.org/A001806)

Offset 4: 24, 600, 10800, 176400, 2822400, 45722880, 762048000, 13172544000, …

### Python 3 — 43 bytes

```python
a=n=4
while[print(a*6)]:n+=1;a=a*n*n//(n-4)
```

**How it works**

- C(n, 4)/C(n − 1, 4) = n/(n − 4), so a(n) = n!·C(n, 4) satisfies
  a(n) = a(n − 1)·n·n/(n − 4).
- `a` holds a(n)/6 = n!·C(n, 4)/6, an integer because 6 divides n! for
  n ≥ 3. It obeys the same ratio, and at n = 4 it is 24/6 = 4 = n, so one
  chained assignment `a=n=4` starts both; printing `a*6` costs 2 bytes,
  while the plain start `a=24;n=4` costs 3.
- Each pass moves `n` on and applies the ratio; the quotient is the
  integer a(n)/6, so the floor division is exact.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- E.g.f. x⁴/(1 − x)⁵. Family n!·C(n, k): [A001804](../A001804/) (k = 2),
  [A001805](../A001805/) (k = 3), A001806 (k = 4),
  [A001807](../A001807/) (k = 5).
- a(1555) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 97 terms (n = 4 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001806), CC BY-SA 4.0.
