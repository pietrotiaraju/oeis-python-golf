# A001538

> a(n) = (12*n+1)*(12*n+11).
> — [OEIS A001538](https://oeis.org/A001538)

Offset 0: 11, 299, 875, 1739, 2891, 4331, 6059, 8075, 10379, 12971, 15851, …

### Python 3 — 30 bytes

```python
n=6
while[print(n*n-25)]:n+=12
```

**How it works**

- The factors 12n + 1 and 12n + 11 lie 5 on either side of their midpoint
  m = 12n + 6, so a(n) = (m − 5)(m + 5) = m² − 25. The counter `n` holds m: it
  starts at 6 and steps by 12, and `n*n-25` is printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Keeping the counter on the first factor, m = 12n + 1, gives `n*(n+10)`,
  2 bytes longer; the expanded 144n² + 144n + 11 in a plain counter costs
  far more, and `while 1:` with the print in the body 2 bytes more.
- A search over every polynomial expression E of up to 9 characters (n,
  constants up to 99, `+ - * **`, unary `-` and `~`, and a final `//` or `>>`)
  in the loop `n=c` / `while[print(E)]:n+=s`, for every start c and step s,
  found nothing shorter.
- Exact integers, so every term is right.
- The b-file has 1001 terms (n = 0 to 1000) and all of them print at once; the
  bar is the whole b-file in 60 s.
- The family (kn + 1)(kn + k − 1): [A001504](../A001504/) (k = 3),
  [A001539](../A001539/) (4), [A001545](../A001545/) (5), [A001513](../A001513/)
  (6), [A001526](../A001526/) (7), [A001533](../A001533/) (8),
  [A001534](../A001534/) (9), [A001535](../A001535/) (10),
  [A001536](../A001536/) (11), [A001538](../A001538/) (12). Even k gets a
  difference of squares, odd k a product with the first factor.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 30 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001538), CC BY-SA 4.0.
