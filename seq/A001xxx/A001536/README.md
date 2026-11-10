# A001536

> a(n) = (11*n+1)*(11*n+10).
> — [OEIS A001536](https://oeis.org/A001536)

Offset 0: 10, 252, 736, 1462, 2430, 3640, 5092, 6786, 8722, 10900, 13320, …

### Python 3 — 31 bytes

```python
n=1
while[print(n*(n+9))]:n+=11
```

**How it works**

- With m = 11n + 1 the factors are m and m + 9, so a(n) = m(m + 9). The
  counter `n` holds m: it starts at 1 and steps by 11, and `n*(n+9)` is
  printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- For odd k the midpoint 11n + 11/2 of the factors is not an integer, so the
  difference of squares of [A001533](../A001533/) needs the doubled counter
  x = 22n + 11: a(n) = (x² − 81)/4, and `n=11` /
  `while[print(n*n-81>>2)]:n+=22` is 3 bytes longer.
- The counter on the second factor, `n=10` with `n*(n-9)`, is 1 byte longer,
  and `n=6` with `n*~-n-20`, since (m − 5)(m + 4) = m² − m − 20 for m = 11n +
  6, is 1 byte longer.
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
| 2026-11-10 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001536), CC BY-SA 4.0.
