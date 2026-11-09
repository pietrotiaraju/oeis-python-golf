# A001288

> a(n) = binomial(n,11).
> — [OEIS A001288](https://oeis.org/A001288)

Offset 11: 1, 12, 78, 364, 1365, 4368, 12376, 31824, 75582, 167960, …

### Python 3 — 37 bytes

```python
a=j=1
while[print(a)]:a+=a*11//j;j+=1
```

**How it works**

- With j = n − 10, the printed `a` is C(j+10, 11) = C(n, 11), starting from
  C(11, 11) = 1 at j = 1, so no zeros and no offset handling are needed.
- **The step is Pascal's rule.** C(n+1, 11) = C(n, 11) + C(n, 10), and
  11·C(n, 11)/j = 11·n!/(11!·(j−1)!·j) = n!/(10!·j!) = C(n, 10). So
  `a+=a*11//j` adds exactly C(n, 10): the floor division is exact.
- The same frame is the record of the C(n, 7) column,
  [A000580](../../A000xxx/A000580/), with 11 in place of 7.

**Notes**

- The ratio form `a=a*(j+11)//j` is 3 bytes longer, and
  `math.comb(n,11)` with `import math` and a counter is 51.
- Exact integer arithmetic, so the program is right for every n; a(n) < n¹¹,
  so the 4300-digit int-to-str limit is far out of reach.
- The b-file has 990 terms (up to a(1000)); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001288), CC BY-SA 4.0.
