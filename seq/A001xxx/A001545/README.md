# A001545

> a(n) = (5*n+1)*(5*n+4).
> — [OEIS A001545](https://oeis.org/A001545)

Offset 0: 4, 54, 154, 304, 504, 754, 1054, 1404, 1804, 2254, 2754, 3304, …

### Python 3 — 30 bytes

```python
n=1
while[print(n*(n+3))]:n+=5
```

**How it works**

- With m = 5n + 1 the factors are m and m + 3, so a(n) = m(m + 3). The
  counter `n` holds m: it starts at 1 and steps by 5, and `n*(n+3)` is
  printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- For odd k the midpoint 5n + 5/2 of the factors is not an integer, so the
  difference of squares of [A001533](../A001533/) needs the doubled counter
  x = 10n + 5: a(n) = (x² − 9)/4, and `n=5` /
  `while[print(n*n-9>>2)]:n+=10` is 2 bytes longer.
- Two other forms tie: the counter on the second factor, `n=4` with `n*(n-3)`,
  and `n=3` with `n*~-n-2`, since (m − 2)(m + 1) = m² − m − 2 for m = 5n + 3.
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
Sequences](https://oeis.org/A001545), CC BY-SA 4.0.
