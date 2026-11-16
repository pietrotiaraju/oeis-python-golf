# A001805

> a(n) = n! * binomial(n,3).
> — [OEIS A001805](https://oeis.org/A001805)

Offset 3: 6, 96, 1200, 14400, 176400, 2257920, 30481920, 435456000, 6586272000, …

### Python 3 — 43 bytes

```python
a=6;n=3
while[print(a)]:n+=1;a=a*n*n//(n-3)
```

**How it works**

- C(n, 3)/C(n − 1, 3) = n/(n − 3), so a(n) = n!·C(n, 3) satisfies
  a(n) = a(n − 1)·n·n/(n − 3).
- `a` starts at a(3) = 3!·1 = 6; each pass moves `n` on and applies the
  ratio, `a=a*n*n//(n-3)`. The quotient is the integer a(n), so the floor
  division is exact and every term is right.

**Notes**

- Same length: `a=n=3` / `while[print(a*2)]:n+=1;a=a*n*n//(n-3)`, where
  `a` holds a(n)/2 (which is 3 = n at the start). With n! itself,
  `f*n*~-n*(n-2)//6`, it is 48 bytes.
- E.g.f. x³/(1 − x)⁴. Family n!·C(n, k): [A001804](../A001804/) (k = 2),
  A001805 (k = 3), [A001806](../A001806/) (k = 4),
  [A001807](../A001807/) (k = 5); [A001810](../A001810/) is a(n)/6.
- a(1556) is the first term over 4300 digits, so Python's int-to-str limit
  stops the program there (an interpreter limit, not a wrong term).
- The b-file has 98 terms (n = 3 to 100); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001805), CC BY-SA 4.0.
