# A000065

> -1 + number of partitions of n.
> — [OEIS A000065](https://oeis.org/A000065)

Offset 0: 0, 0, 1, 2, 4, 6, 10, 14, 21, 29, 41, 55, 76, 100, 134, 175, …

Also the number of partitions of n into parts smaller than n, and the
number of rooted trees on n + 1 nodes with height exactly 2.

### Python 3 — 81 bytes

```python
*a,n=1,0
while[print(a[-1]-1)]:n-=1;a+=sum(d*sum(a[d::d])for d in range(n,0))//n,
```

**How it works**

- This is the [A000041](../A000041/) program with `-1` in the print: the
  list holds the partition numbers p(0), p(1), … and each one is printed
  less one.
- The terms come from **N·p(N) = Σ_d d·Σ_j p(N − dj)** over d = 1…N and
  j ≥ 1 with dj ≤ N, the log derivative of Π 1/(1 − xᵏ) with σ(k) split
  into its divisors. `n` is −N, so `d` runs over −N…−1, the slice
  `a[d::d]` is p(N − |d|), p(N − 2|d|), …, the sum is −N·p(N) and `//n`
  divides it out exactly.
- `*a,n=1,0` sets a = [1] and n = 0, and `while[print(…)]:` prints in the
  loop condition, since `[None]` is true.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The whole b-file (1001 terms) prints in under a second; the bar is the
  whole b-file in 60 s.
- Storing −p(n) instead, with `*a,n=-1,0` and `print(~a[-1])`, is also
  81 bytes: the seed costs the byte that `~` saves.
- Excluding the part N (`range(n+1,0)`) gives p(N) − 1 directly, but the
  list then needs p(N) again for the later terms, so it is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 81 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000065), CC BY-SA 4.0.
