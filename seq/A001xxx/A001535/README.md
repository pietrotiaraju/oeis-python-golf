# A001535

> a(n) = (10n+1)*(10n+9).
> — [OEIS A001535](https://oeis.org/A001535)

Offset 0: 9, 209, 609, 1209, 2009, 3009, 4209, 5609, 7209, 9009, 11009, …

### Python 3 — 30 bytes

```python
n=5
while[print(n*n-16)]:n+=10
```

**How it works**

- The factors 10n + 1 and 10n + 9 lie 4 on either side of their midpoint
  m = 10n + 5, so a(n) = (m − 4)(m + 4) = m² − 16. The counter `n` holds m: it
  starts at 5 and steps by 10, and `n*n-16` is printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- Keeping the counter on the first factor, m = 10n + 1, gives `n*(n+8)`,
  1 byte longer; the expanded 100n² + 100n + 9 in a plain counter costs
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
Sequences](https://oeis.org/A001535), CC BY-SA 4.0.
