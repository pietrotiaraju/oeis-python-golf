# A000582

> a(n) = binomial coefficient C(n,9).
> — [OEIS A000582](https://oeis.org/A000582)

Offset 9: 1, 10, 55, 220, 715, 2002, 5005, 11440, 24310, 48620, …

### Python 3 — 36 bytes

```python
a=j=1
while[print(a)]:a+=a*9//j;j+=1
```

**How it works**

- With j = n − 8, the printed `a` is C(j+8, 9) = C(n, 9), starting from
  C(9, 9) = 1 at j = 1, so no zeros and no offset handling are needed.
- **The step is Pascal's rule.** C(n+1, 9) = C(n, 9) + C(n, 8), and
  9·C(n, 9)/j = 9·n!/(9!·(j−1)!·j) = n!/(8!·j!) = C(n, 8). So
  `a+=a*9//j` adds exactly C(n, 8): the floor division is exact.
- This is 3 bytes under the ratio form `a=a*(j+9)//j` and needs no
  parentheses.

**Notes**

- Other versions that print the same terms: the ratio form,
  `a=j=1` / `while[print(a)]:a=a*(j+9)//j;j+=1`: 39 bytes; with n itself,
  `n=9;a=1` / `while[print(a)]:n+=1;a=a*n//(n-9)`: 41 bytes;
  `math.comb(n,9)` with `import math`: 49 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 992 terms (up to a(1000)); the bar is the whole b-file in
  60 s, and the program prints it in about 0.1 s here.
- a(n) < n⁹, so the 4300-digit int-to-str limit is far out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 50 | first entry |
| 2026-11-06 | Python 3 | 41 | advance the binomial column by its exact ratio |
| 2026-11-07 | Python 3 | 36 | Pascal step `a+=a*9//j` with j = n − 8 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000582), CC BY-SA 4.0.
