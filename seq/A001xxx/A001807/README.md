# A001807

> a(n) = n! * binomial(n,5).
> — [OEIS A001807](https://oeis.org/A001807)

Offset 5: 120, 4320, 105840, 2257920, 45722880, 914457600, 18441561600, 379369267200, …

### Python 3 — 44 bytes

```python
a=n=5
while[print(a*24)]:n+=1;a=a*n*n//(n-5)
```

**How it works**

- C(n, 5)/C(n − 1, 5) = n/(n − 5), so a(n) = n!·C(n, 5) satisfies
  a(n) = a(n − 1)·n·n/(n − 5).
- `a` holds a(n)/24 = n!·C(n, 5)/24, an integer because 24 divides n! for
  n ≥ 4. It obeys the same ratio, and at n = 5 it is 120/24 = 5 = n, so
  `a=n=5` starts both; printing `a*24` costs 3 bytes, the plain start
  `a=120;n=5` 4.
- Each pass moves `n` on and applies the ratio; the quotient is the
  integer a(n)/24, so the floor division is exact.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- E.g.f. x⁵/(1 − x)⁶. Family n!·C(n, k): [A001804](../A001804/) (k = 2),
  [A001805](../A001805/) (k = 3), [A001806](../A001806/) (k = 4),
  A001807 (k = 5).
- a(1554) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 96 terms (n = 5 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001807), CC BY-SA 4.0.
