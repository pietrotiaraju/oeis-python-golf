# A001526

> a(n) = (7*n+1)*(7*n+6).
> — [OEIS A001526](https://oeis.org/A001526)

Offset 0: 6, 104, 300, 594, 986, 1476, 2064, 2750, 3534, 4416, 5396, 6474, …

### Python 3 — 30 bytes

```python
n=1
while[print(n*(n+5))]:n+=7
```

**How it works**

- With m = 7n + 1 the factors are m and m + 5, so a(n) = m(m + 5). The
  counter `n` holds m: it starts at 1 and steps by 7, and `n*(n+5)` is
  printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- For odd k the midpoint 7n + 7/2 of the factors is not an integer, so the
  difference of squares of [A001533](../A001533/) needs the doubled counter
  x = 14n + 7: a(n) = (x² − 25)/4, and `n=7` /
  `while[print(n*n-25>>2)]:n+=14` is 3 bytes longer.
- Two other forms tie: the counter on the second factor, `n=6` with `n*(n-5)`,
  and `n=4` with `n*~-n-6`, since (m − 3)(m + 2) = m² − m − 6 for m = 7n + 4.
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
Sequences](https://oeis.org/A001526), CC BY-SA 4.0.
