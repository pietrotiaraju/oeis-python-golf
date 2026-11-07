# A000581

> a(n) = binomial coefficient C(n,8).
> — [OEIS A000581](https://oeis.org/A000581)

Offset 8: 1, 9, 45, 165, 495, 1287, 3003, 6435, 12870, 24310, …

### Python 3 — 36 bytes

```python
a=j=1
while[print(a)]:a+=a*8//j;j+=1
```

**How it works**

- With j = n − 7, the printed `a` is C(j+7, 8) = C(n, 8), starting from
  C(8, 8) = 1 at j = 1, so no zeros and no offset handling are needed.
- **The step is Pascal's rule.** C(n+1, 8) = C(n, 8) + C(n, 7), and
  8·C(n, 8)/j = 8·n!/(8!·(j−1)!·j) = n!/(7!·j!) = C(n, 7). So
  `a+=a*8//j` adds exactly C(n, 7): the floor division is exact.
- This is 3 bytes under the ratio form `a=a*(j+8)//j` and needs no
  parentheses.

**Notes**

- Other versions that print the same terms: the ratio form,
  `a=j=1` / `while[print(a)]:a=a*(j+8)//j;j+=1`: 39 bytes; with n itself,
  `n=8;a=1` / `while[print(a)]:n+=1;a=a*n//(n-8)`: 41 bytes;
  `math.comb(n,8)` with `import math`: 49 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 993 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < n⁸, so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |
| 2026-11-07 | Python 3 | 36 | Pascal step `a+=a*8//j` with j = n − 7 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000581), CC BY-SA 4.0.
