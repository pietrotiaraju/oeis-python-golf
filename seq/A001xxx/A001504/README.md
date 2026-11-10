# A001504

> a(n) = (3*n+1)*(3*n+2).
> — [OEIS A001504](https://oeis.org/A001504)

Offset 0: 2, 20, 56, 110, 182, 272, 380, 506, 650, 812, 992, 1190, 1406, …

### Python 3 — 28 bytes

```python
n=1
while[print(n*n+n)]:n+=3
```

**How it works**

- With m = 3n + 1 the factors are m and m + 1, so a(n) = m(m + 1) = m² + m.
  The counter `n` holds m: it starts at 1 and steps by 3, and `n*n+n` is
  printed.
- `print(…)` runs in the loop condition and returns `None`; `[None]` is a
  non-empty list, so the loop never ends and its body only steps the counter.

**Notes**

- `n*-~n` (`-~n` is n + 1) and `n*~-n` from m = 3n + 2 tie. Completing the
  square with the odd x = 6n + 3 gives x² = 4a(n) + 1 and `n*n//4` (step 6),
  1 byte longer; `while 1:` with the print in the body is 2 bytes longer.
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
  difference of squares, odd k a product with the first factor. Here k = 3 is the one odd k where m(m + 1) needs no constant.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 28 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001504), CC BY-SA 4.0.
