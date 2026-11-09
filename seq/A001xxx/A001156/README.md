# A001156

> Number of partitions of n into squares.
> — [OEIS A001156](https://oeis.org/A001156)

Offset 0: 1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 4, …

### Python 3 — 88 bytes

```python
*a,n=1,0
while[print(a[-1])]:n-=1;a+=sum(d*d*sum(a[-d*d::-d*d])for d in range(n,0))//-n,
```

**How it works**

- The Euler transform of the squares: with b(k) the sum of the square
  divisors of k ([A035316](https://oeis.org/A035316)),
  n·a(n) = Σ_{k=1..n} b(k)·a(n−k). Grouping by the square d² gives
  n·a(n) = Σ_d d²·(a(n−d²) + a(n−2d²) + …).
- The list `a` holds a(0), …, a(n−1). For d < 0 (`range(n,0)` with n
  negative, as in the partition program [A000041](../../A000xxx/A000041/)),
  `a[-d*d::-d*d]` starts d² places from the end and steps back by d², so it
  is exactly a(n−d²), a(n−2d²), …; for d² > n the slice is empty.
- `n` counts down (−1, −2, …), so `//-n` divides by the positive index. The
  sum is always a multiple of n, so the division is exact.

**Notes**

- Exact for every n: integer arithmetic only.
- The loop over d runs to n rather than √n (empty slices cost nothing but
  the loop step), so the time grows like n². The bar is 8000 of the 10001
  b-file terms in 60 s (about 22 s here); the whole b-file takes about 28–33 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001156), CC BY-SA 4.0.
