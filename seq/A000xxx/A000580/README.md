# A000580

> a(n) = binomial coefficient C(n,7).
> — [OEIS A000580](https://oeis.org/A000580)

Offset 7: 1, 8, 36, 120, 330, 792, 1716, 3432, 6435, 11440, …

### Python 3 — 36 bytes

```python
a=j=1
while[print(a)]:a+=a*7//j;j+=1
```

**How it works**

- With j = n − 6, the printed `a` is C(j+6, 7) = C(n, 7), starting from
  C(7, 7) = 1 at j = 1, so no zeros and no offset handling are needed.
- **The step is Pascal's rule.** C(n+1, 7) = C(n, 7) + C(n, 6), and
  7·C(n, 7)/j = 7·n!/(7!·(j−1)!·j) = n!/(6!·j!) = C(n, 6). So
  `a+=a*7//j` adds exactly C(n, 6): the floor division is exact.
- This is 3 bytes under the ratio form `a=a*(j+7)//j` and needs no
  parentheses.

**Notes**

- Other versions that print the same terms: the ratio form,
  `a=j=1` / `while[print(a)]:a=a*(j+7)//j;j+=1`: 39 bytes; with n itself,
  `n=7;a=1` / `while[print(a)]:n+=1;a=a*n//(n-7)`: 41 bytes;
  `math.comb(n,7)` with `import math`: 49 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 994 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < n⁷, so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |
| 2026-11-07 | Python 3 | 36 | Pascal step `a+=a*7//j` with j = n − 6 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000580), CC BY-SA 4.0.
