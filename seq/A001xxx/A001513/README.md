# A001513

> a(n) = (6*n+1)*(6*n+5).
> — [OEIS A001513](https://oeis.org/A001513)

Offset 0: 5, 77, 221, 437, 725, 1085, 1517, 2021, 2597, 3245, 3965, 4757, …

### Python 3 — 28 bytes

```python
n=3
while[print(n*n-4)]:n+=6
```

**How it works**

- The factors 6n + 1 and 6n + 5 lie 2 on either side of their midpoint
  m = 6n + 3, so a(n) = (m − 2)(m + 2) = m² − 4. The counter `n` holds m: it
  starts at 3 and steps by 6, and `n*n-4` is printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Keeping the counter on the first factor, m = 6n + 1, gives `n*(n+4)`,
  2 bytes longer; the expanded 36n² + 36n + 5 in a plain counter costs
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
| 2026-11-10 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001513), CC BY-SA 4.0.
