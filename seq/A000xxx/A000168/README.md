# A000168

> a(n) = 2*3^n*(2*n)!/(n!*(n+2)!).
> — [OEIS A000168](https://oeis.org/A000168)

Offset 0: 1, 2, 9, 54, 378, 2916, 24057, 208494, 1876446, 17399772, …

### Python 3 — 43 bytes

```python
a=1;m=3
while[print(a)]:a=12*a-30*a//m;m+=1
```

**How it works**

- The ratio of consecutive terms is a(n)/a(n−1) = 6(2n−1)/(n+2). With
  m = n+2 this is a(n) = a(n−1)·(12m−30)/m = 12·a(n−1) − 30·a(n−1)/m.
- Because a(n) is an integer, m divides a(n−1)·(12m−30) and hence
  30·a(n−1): the split form `12*a-30*a//m` is exact and two bytes under
  `a*=12*m-30;a//=m`.
- `m` starts at 3 for a(1) = 2.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (926 terms) prints at once; the program stops after a(3992), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000168), CC BY-SA 4.0.
