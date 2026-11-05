# A000164

> Number of partitions of n into 3 squares (allowing part zero).
> — [OEIS A000164](https://oeis.org/A000164)

Offset 0: 1, 1, 1, 1, 1, 1, 1, 0, 1, 2, …

### Python 3 — 79 bytes

```python
s=[n:=0]
while[print(sum(j<=k<=n-j-k in s for j in s for k in s))]:n+=1;s+=n*n,
```

**How it works**

- `s` holds the squares 0, 1, 4, …, n², which include every square up
  to n.
- A partition n = j + k + l into three squares with j ≤ k ≤ l is counted
  once, by its two smallest parts. The chained comparison
  `j<=k<=n-j-k in s` means `j <= k`, `k <= n-j-k` and `n-j-k in s`.
- `s=[n:=0]` sets up the list and the counter in one statement; each step
  appends the next square with `s+=n*n,`.
- The direct triple loop over `range` (`a*a+b*b+c*c==n for a in
  range(n+1)…`) is 100 bytes, 96 with `R=range`.

**Notes**

- Exact integer arithmetic, correct for every n. A term costs O(n²)
  steps of the double loop; the list scan only runs when the first two
  tests pass. About 1030 terms come out in 60 s on the machine that set
  the bar, which is 800 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000164), CC BY-SA 4.0.
