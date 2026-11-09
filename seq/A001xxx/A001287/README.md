# A001287

> a(n) = binomial coefficient C(n,10).
> — [OEIS A001287](https://oeis.org/A001287)

Offset 10: 1, 11, 66, 286, 1001, 3003, 8008, 19448, 43758, 92378, …

### Python 3 — 37 bytes

```python
a=j=1
while[print(a)]:a+=a*10//j;j+=1
```

**How it works**

- With j = n − 9, the printed `a` is C(j+9, 10) = C(n, 10), starting from
  C(10, 10) = 1 at j = 1, so no zeros and no offset handling are needed.
- **The step is Pascal's rule.** C(n+1, 10) = C(n, 10) + C(n, 9), and
  10·C(n, 10)/j = 10·n!/(10!·(j−1)!·j) = n!/(9!·j!) = C(n, 9). So
  `a+=a*10//j` adds exactly C(n, 9): the floor division is exact.
- The same frame is the record of the C(n, 7) column,
  [A000580](../../A000xxx/A000580/), with 10 in place of 7.

**Notes**

- The ratio form `a=a*(j+10)//j` is 3 bytes longer, and
  `math.comb(n,10)` with `import math` and a counter is 51.
- Exact integer arithmetic, so the program is right for every n; a(n) < n¹⁰,
  so the 4300-digit int-to-str limit is far out of reach.
- The b-file has 991 terms (up to a(1000)); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001287), CC BY-SA 4.0.
